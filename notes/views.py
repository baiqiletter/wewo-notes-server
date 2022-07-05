import json

from django.http import HttpResponse, JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.http import require_http_methods

from . import db


# Create your views here.


@require_http_methods(['GET'])
def home(request):
    try:
        username = request.GET['username']
        user_id = db.find_user_id(username)
        notes = [db.check_tags_and_links(n_id) for n_id in db.find_all_notes(user_id=user_id)]
        total_tags = set()
        for n in notes:
            for tag in n['tags']:
                total_tags.add(tag)
        total_tags = list(total_tags)
        return JsonResponse({
            'user_id': user_id,
            'user_name': username,
            'notes': notes,
            'total_tags': total_tags,
        })
    except MultiValueDictKeyError:
        return HttpResponse('未登录')


@require_http_methods(['POST'])
def register(request):
    if request.method == 'POST':
        username = json.loads(request.body).get('username')
        password = json.loads(request.body).get('password')
        if db.register(username, password):
            return JsonResponse({'code': 1, 'message': '注册成功', 'username': username})
        else:
            return JsonResponse({'code': 0, 'message': '该用户名已存在', 'username': username})


@require_http_methods(['POST'])
def login(request):
    if request.method == 'POST':
        username = json.loads(request.body).get('username')
        password = json.loads(request.body).get('password')
        if db.login(username, password):
            return JsonResponse({'code': 1, 'message': '登陆成功', 'username': username})
        else:
            return JsonResponse({'code': 0, 'message': '用户名或密码错误', 'username': username})


@require_http_methods(['POST'])
def note_add(request):
    username = json.loads(request.body).get('username')
    user_id = db.find_user_id(username)
    content = json.loads(request.body).get('content')
    note_id = db.write_note(owner_id=user_id, content=content)
    added_note = db.check_tags_and_links(note_id)
    return JsonResponse({
        'code': 1,
        'message': '笔记添加成功',
        'username': username,
        'added_note': added_note
    })


@require_http_methods(['POST'])
def note_del(request):
    username = json.loads(request.body).get('username')
    user_id = db.find_user_id(username)
    note_id = json.loads(request.body).get('note_id')
    if db.delete_note(owner_id=user_id, note_id=note_id):
        return JsonResponse({'code': 1, 'message': '笔记删除成功', 'username': username, 'note_id': note_id})
    else:
        return JsonResponse({'code': 0, 'message': '笔记删除失败', 'username': username, 'note_id': note_id})


@require_http_methods(['GET', 'POST'])
def note(request, note_id):
    if request.method == 'GET':  # 获取笔记详情
        # 从数据库获取笔记
        # content = db.find_note(note_id=note_id).content
        # tags = [t[1:] for t in re.compile(r'#\S+').findall(content)]
        # links = [t[12:] for t in re.compile(r'link://note/\S+').findall(content)]
        main_note = db.check_tags_and_links(note_id)
        linked_notes = [db.check_tags_and_links(n_id) for n_id in main_note['links']]
        # linked_notes_id = [db.find_note(t) for t in main_note['links']]
        # linked_notes = [{'note_id': n.id, 'content': n.content, 'tags': [], 'links': []} for n in linked_notes_id]
        return JsonResponse({
            'main_note': main_note,
            'linked_notes': linked_notes
        })
    elif request.method == 'POST':  # 修改笔记
        # 写入数据库
        username = request.POST.get('username')
        user_id = db.find_user_id(username)
        content = json.loads(request.body).get('content')
        result, msg = db.modify_note(note_id=note_id, user_id=user_id, new_content=content)
        if result:
            modified_note = db.check_tags_and_links(note_id)
            return JsonResponse({
                'code': 1,
                'message': msg,
                'modified_note': modified_note,
            })
        else:
            return JsonResponse({
                'code': 0,
                'message': msg,
                'modified_note': {},
            })


@require_http_methods(['POST'])
def image_add(request):
    username = request.POST.get('username')
    user_id = db.find_user_id(username)

    new_image = request.FILES.get('file')

    # 将图片存到数据库，获取URL
    image_url = db.add_new_image(owner_id=user_id, image=new_image)
    return JsonResponse({'code': 1, 'url': image_url})


@require_http_methods(['POST'])
def image_del(request):
    # 似乎暂时不需要
    return HttpResponse("删除图片")


# @require_http_methods(['GET'])
# def image(request, image_id):
#     username = request.GET.get('username')
#     user_id = db.find_user_id(username)
#
#     return HttpResponse("查询图片")


@require_http_methods(['GET'])
def get_notes_with_tag(request, tag_name):
    notes = [db.check_tags_and_links(t) for t in db.find_all_notes_with_tag(tag_name)]
    return JsonResponse({
        'tag': tag_name,
        'notes': notes
    })

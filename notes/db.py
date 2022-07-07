import re

from django.db import IntegrityError
from .models import *


# 主页部分
# 查询所有笔记
def find_all_notes(user_id):
    return [n['id'] for n in Note.objects.filter(owner_id_FK_id=user_id).order_by('-update_time').values()]


# 注册
def register(username, password):
    try:
        User(username=username, password=password).save()
        return True
    except IntegrityError:
        return False


# 删除用户
def delete_user(user_id):
    try:
        User.objects.get(id=user_id).delete()
        return True
    except User.DoesNotExist:
        return False


# 登录
def login(username, password):
    try:
        return User.objects.get(username=username).password == password
    except User.DoesNotExist:
        return False


# 根据用户名和密码查id主键
def find_user_id(username):
    try:
        return User.objects.get(username=username).id
    except User.DoesNotExist:
        return None


# 笔记部分
# 新增笔记
def write_note(owner_id, content):
    n = Note(owner_id_FK_id=owner_id, content=content)
    n.save()
    return n.id


# 删除笔记
def delete_note(owner_id, note_id):
    try:
        Note.objects.get(id=note_id, owner_id_FK_id=owner_id).delete()
        return True
    except Note.DoesNotExist:
        return False


# 修改笔记
def modify_note(note_id, user_id, new_content):
    try:
        target = Note.objects.get(id=note_id)
        if target.owner_id_FK_id == user_id:
            target.content = new_content
            target.save()
            return True, "修改成功"
        else:
            return False, "当前用户无权修改该笔记"
    except Note.DoesNotExist:
        return False, "笔记不存在"


# 查询笔记
def find_note(note_id):
    try:
        return Note.objects.get(id=note_id)
    except Note.DoesNotExist:
        return None


# 检查笔记的标签和链接，并维护相关数据表
def check_tags_and_links(note_id):
    note = find_note(note_id)
    if note is None:
        return None
    content = note.content
    tags = [t[1:] for t in re.compile(r'#\S+').findall(content)]
    links = [t[12:] for t in re.compile(r'link://note/[0-9]+').findall(content)]
    # 清除已有标签和链接
    delete_tag(note_id)
    delete_link(note_id)
    # 添加扫描到的标签
    for tag in tags:
        add_new_tag(note_id, tag)
    for link in links:
        add_new_link(note_id, link)
    # 返回完整笔记信息
    return {
        'note_id': note_id,
        'content': content,
        'update_time': note.update_time,
        'tags': tags,
        'links': links,
    }


# 图片部分
# 新增图片
def add_new_image(owner_id, image):
    temp_image = Image(owner_id_FK_id=owner_id, image=image)
    temp_image.save()
    return temp_image.image.url


# 删除图片
def delete_image(image_id):
    Image.objects.filter(id=image_id).delete()
    return True


# 查询图片
def find_image(image_id):
    return Image.objects.get(id=image_id)


# 标签部分
# 新增标签
def add_new_tag(note_id, tag_name):
    temp_tag = Tag(note_id_FK_id=note_id, tag_name=tag_name)
    temp_tag.save()
    return True


# 查询笔记所有标签
def find_note_tags(note_id):
    return [t['tag_name'] for t in Tag.objects.filter(note_id_FK_id=note_id).values()]


# 删除某个笔记的所有标签
def delete_tag(note_id):
    Tag.objects.filter(note_id_FK_id=note_id).delete()
    return True


# 查询有特定标签的所有笔记
def find_all_notes_with_tag(tag_name):
    return [n.note_id_FK_id for n in Tag.objects.filter(tag_name=tag_name)]


# 链接部分
# 新增链接
def add_new_link(ori_note_id, ref_note_id):
    temp_link = Link(ori_note_id=ori_note_id, ref_note_id=ref_note_id)
    temp_link.save()
    return True


# 查询笔记所有链接
def find_note_links(note_id):
    return [t['ref_note_id'] for t in Link.objects.filter(ori_note_id=note_id).values()]


# 删除某个笔记的所有链接
def delete_link(ori_note_id):
    Link.objects.filter(ori_note_id=ori_note_id).delete()
    return True

from django.urls import path, re_path
from django.views.static import serve

from server.settings import MEDIA_ROOT
from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.mine, name='mine'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('note/add', views.note_add, name='note_add'),
    path('note/delete', views.note_del, name='note_del'),
    path('note/<str:note_id>', views.note, name='note'),
    path('image/add', views.image_add, name='image_add'),
    path('image/<str:image_id>/delete', views.image_del, name='image_del'),
    # path('image/<str:image_id>', views.image, name='image'),
    re_path(r'^image/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT}),
    path('tag/<str:tag_name>', views.get_notes_with_tag, name='get_notes_with_tag'),
]

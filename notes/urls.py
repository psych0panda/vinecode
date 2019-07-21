from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.root_api, name='api-root'),
    path('note_list/', views.NoteList.as_view(), name='note-list'),
    path('note_detail/<int:pk>/', views.NoteDetail.as_view(), name='note-detail'),
    path('user_list', views.UserList.as_view(), name='user-list'),
    path('user_detail/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

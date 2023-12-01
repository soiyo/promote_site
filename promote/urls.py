# promote/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # /promote 로 promote/views.py의 index() 연결
    path('<int:content_id>/', views.detail, name='detail'), # /promote/content_id 로 views.py의 detail() 연결, name을 작성하여 .html url 연동에서 하드코딩 방지
    path('comment/create/<int:content_id>/', views.comment_create, name='comment_create'),
    path('comment/update/<int:comment_id>/', views.comment_update, name='comment_update'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]
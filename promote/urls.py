# promote/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # /promote 로 promote/views.py의 index() 연결
]

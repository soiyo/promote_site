# goods/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage), # mainpage 연결
    path('company/', views.company), # goods/views.py 파일의 company라는 함수를 /company라는 링크에 연결
]

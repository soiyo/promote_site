# accounts/urls.py
# LogoutView는 django.contrib.auth에서 제공하는 기능이라 따로 만들 필요가 없다.
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'
urlpatterns = [
    path ('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path ('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path ('signup/', views.signup, name='signup'),
]


# promote_site/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('promote/', include('promote.urls')), # http://127.0.0.1:8000/promote/ 로 promote/urls.py 파일 연결
    path('', include('goods.urls')),
    path('accounts/', include('accounts.urls')),
]

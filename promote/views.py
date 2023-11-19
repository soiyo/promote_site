# promote/views.py
from django.shortcuts import render # content_list 데이터를 promote/content_list.html 파일에 적용 후 HTML 리턴
from .models import MainContent
# Create your views here.

def index(request):
    content_list = MainContent.objects.order_by('-pub_date') # 역순 정렬(가장 최신 콘텐츠를 상단에 노출)
    context = {'content_list': content_list}
    return render(request, 'promote/content_list.html', context)
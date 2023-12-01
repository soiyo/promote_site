# promote/views.py
from django.shortcuts import get_object_or_404, render
# get_object_or_404 : 404 오류 발생시 연결해줄 view (사용 안할시 DoesNotExist 오류 뜸, 사용시 Page not found(404) 뜨게 해줌)
# render : content_list 데이터를 promote/content_list.html 파일에 적용 후 HTML 리턴
from .models import MainContent

# Create your views here.

def index(request):
    content_list = MainContent.objects.order_by('-pub_date') # 역순 정렬(가장 최신 콘텐츠를 상단에 노출)
    context = {'content_list': content_list}
    return render(request, 'promote/content_list.html', context)

def detail(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)
    # content_list = MainContent.objects.get(id=content_id) # content_id 를 가져옴
    context = {'content_list': content_list}
    return render(request, 'promote/content_detail.html', context)
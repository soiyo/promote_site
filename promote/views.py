# promote/views.py
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
# get_object_or_404 : 404 오류 발생시 연결해줄 view (사용 안할시 DoesNotExist 오류 뜸, 사용시 Page not found(404) 뜨게 해줌)
# render : content_list 데이터를 promote/content_list.html 파일에 적용 후 HTML 리턴
from .models import MainContent, Comment
from .forms import CommentForm

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

@login_required(login_url='accounts:login')
def comment_create(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content_list = content_list
            comment.author = request.user
            comment.save()
            return redirect('detail', content_id=content_list.id)
    else:
        form = CommentForm()
    context = {'content_list':content_list, 'form':form}
    return render(request, 'promote/content_detail.html', context)
    
    
# 비로그인 상태에서 댓글 작성 시 로그인 화면으로 이동하는 코드 추가    
@login_required(login_url='accounts:login')
def comment_create(request, content_id):
    content_list = get_object_or_404(MainContent, pk=content_id)
    
# 로그인 시에만 가능하게 하고 if request.user != comment.author로 작성자가 아닌 사용자가 update를 시도하면 PermissionDenied 오류를 일으킨다.
@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment) #수정시 최초 작성했던 댓글을 화면에 출력하기 위한 코드
    context = {'comment': comment, 'form': form}
    return render(request, 'promote/comment_form.html', context)
    
@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        raise PermissionDenied
    else:
        comment.delete() #삭제
    return redirect('detail', content_id=comment.content_list.id)
    

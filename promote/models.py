from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MainContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date_published')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    #자신과 다대일 관계만들려면 : models.ForeignKey('self', on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True) # 최초 시간 저장
    modify_date = models.DateTimeField(auto_now=True) # 댓글 수정시 수정 시간 정함
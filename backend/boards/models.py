from django.db import models
from django.conf import settings

# Create your models here.
class Counting(models.Model):
    ip = models.CharField(max_length=50)

class Board(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    group_order = models.IntegerField(default=0) # 게시글 id
    order_id = models.IntegerField(default=0) # 댓글 순서
    depth = models.IntegerField(default=0) # 계층
    created_at = models.DateTimeField(auto_now_add=True)
    counting = models.ManyToManyField(Counting, related_name='board_counting')


    

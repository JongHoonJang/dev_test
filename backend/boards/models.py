from django.db import models
from django.conf import settings

# Create your models here.
class Board(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    order_id = models.IntegerField(default=0) # 게시글 ID
    group_order = models.IntegerField(default=0) # 댓글 ID
    depth = models.IntegerField(default=0) # 댓글의 댓글 ID
    created_at = models.DateTimeField(auto_now_add=True)
    
# class Comment(models.Model):
#     user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     board_id = models.ForeignKey(Board, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
    

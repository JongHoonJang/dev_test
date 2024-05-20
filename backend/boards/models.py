from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Board(AbstractUser):
    name = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    

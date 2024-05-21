from rest_framework import serializers
from .models import Board
from django.contrib.auth import get_user_model
User = get_user_model()

class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = (
            'name',
            'title',
            'content',
            'created_at',
        )
class BoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = (
            'id',
            'name',
            'title',
            'content',
            'created_at',         
        )
        
# class CommentListSerializer(serializers.ModelSerializer):

#     class UserSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = User
#             fields = (
#                 'id',
#                 'name'
#             )

#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Comment
#         fields = '__all__'
        



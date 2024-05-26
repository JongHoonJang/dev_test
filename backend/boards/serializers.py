from rest_framework import serializers
from .models import Board
from django.contrib.auth import get_user_model
User = get_user_model()

class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = (
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

#     user_id = UserSerializer(read_only=True)

#     class Meta:
#         model = Comment
#         fields = (
#             'user_id',
#             'title',
#             'content',
#             'created_at',
#         )
        
class BoardDetailSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = (
                'id',
                'name'
            )
            
    user_id = UserSerializer(read_only=True)
    # comment_set = CommentListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Board
        fields = (
            'id',
            'user_id',
            'title',
            'content',
            'order_id',
            'group_order',
            'depth',
            'created_at', 
            # 'comment_set',        
        )
        
        



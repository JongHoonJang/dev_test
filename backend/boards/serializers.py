from rest_framework import serializers
from .models import Board,Counting
from django.contrib.auth import get_user_model
User = get_user_model()

class CountingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counting
        fields = '__all__'

class BoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = (
            'id',
            'title',
            'content',
            'created_at',
        )

        
class BoardListSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = (
                'id',
                'name'
            )
            
    user_id = UserSerializer(read_only=True)
    counting = CountingSerializer(many=True, read_only=True)
    board_counting = serializers.IntegerField(source='counting.count',read_only=True)
    class Meta:
        model = Board
        fields = (
            'id',
            'user_id',
            'title',
            'depth',
            'created_at', 
            'counting',
            'board_counting',       
        )
        read_only_fields = ('counting', 'board_counting' )
        



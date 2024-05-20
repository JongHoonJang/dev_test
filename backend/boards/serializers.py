from rest_framework import serializers
from .models import Board

class BoardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = (
            'name',
            'title',
            'content',
            'created_at',
            'updated_at', 
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
            'updated_at',            
        )

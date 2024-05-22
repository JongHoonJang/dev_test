from backend.common import checkuser
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Board, Comment
from .serializers import BoardCreateSerializer, BoardDetailSerializer, CommentListSerializer


# Create your views here.
@api_view(["GET"])
def board_list(request):
    if request.method == "GET":
        boards = Board.objects.order_by("id")
        serializer = BoardDetailSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(["POST"])
def board_create(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    user_token = checkuser(token)
    user = get_object_or_404(get_user_model(), id=user_token)
    if request.method == "POST":
        serializer = BoardCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=user)
        return Response(status=status.HTTP_201_CREATED)
    
@api_view(["GET", "PUT", "DELETE"])
def board_detail_or_update_or_delete(request):
    board_id = request.data.get("id")
    borad = get_object_or_404(Board, id=board_id)
    token = request.META.get("HTTP_AUTHORIZATION")
    user_token = checkuser(token)
    user = get_object_or_404(get_user_model(), id=user_token)
    
    if request.method == "GET":
        serializer = BoardDetailSerializer(borad)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = BoardDetailSerializer(instance=borad, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=user)
        return Response(status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        borad.delete()
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['GET', 'POST'])
def comment_list_or_create(request, board_id):
    token = request.META.get("HTTP_AUTHORIZATION")
    user_token = checkuser(token)
    user = get_object_or_404(get_user_model(), id=user_token)
    board = get_object_or_404(Board, id=board_id)

    if request.method == 'GET':
        comments = board.comment_set.order_by('-id')
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CommentListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(board_id=board, user_id=user)

            comments = board.comment_set.order_by('-id')
            serializer = CommentListSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, board_id, comment_id):
    token = request.META.get("HTTP_AUTHORIZATION")
    user_id = checkuser(token)
    user = get_object_or_404(get_user_model(), id=user_id)
    board = get_object_or_404(Board, id=board_id)
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.method == 'PUT':
        if user == comment.user:
            serializer = CommentListSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(board=board, user=user)
                comments = board.comment_set.order_by('-id')
                serializer = CommentListSerializer(comments, many=True)
                return Response(serializer.data)
    elif request.method == 'DELETE':
        if user == comment.user:
            comment.delete()
            comments = board.comment_set.order_by('-id')
            serializer = CommentListSerializer(comments, many=True)
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
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
    token = request.data.get('headers').get('Authorization')
    user_token = checkuser(token)
    user = get_object_or_404(get_user_model(), id=user_token)
    board = request.data.get("data")
    # 새글 작성일 경우
    if request.POST['no'] == '-1':
        value = Board.objects.aggregate(max_group_order=max('group_order'))
        board.group_order = value['max_group_order'] + 1
    # 답글 작성일 경우 order_id, group_order, depth 설정
    else:
        board2 = Board.objects.get(id=request.POST['no'])
        # 답글이 작성될 경우, 작성되는 답글의 order_id+1보다 크거나 같은 그룹 내의 이전 게시글의 order_id +1씩 올려주어야 한다.
        Board.objects.filter(order_id__gte=board2.order_id + 1).update(order_id=('order_id') + 1)
        board.group_order = board2.group_order
        board.order_id = board2.order_id + 1
        board.depth = board2.depth + 1
        
    if request.method == "POST":
        serializer = BoardCreateSerializer(data=board)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=user)
        return Response(status=status.HTTP_201_CREATED)
    
@api_view(["GET", "PUT", "DELETE"])
def board_detail_or_update_or_delete(request, board_id):
    borad = get_object_or_404(Board, id=board_id)
    
    if request.method == "GET":
        serializer = BoardDetailSerializer(borad)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    token = request.data.get('headers').get('Authorization')
    user_token = checkuser(token)
    user = get_object_or_404(get_user_model(), id=user_token)
    print(request.data.get("data"))
    if request.method == "PUT":
        serializer = BoardDetailSerializer(instance=borad, data=request.data.get("data"))
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=user)
        return Response(status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        borad.delete()
        return Response(status=status.HTTP_200_OK)

    return Response(status=status.HTTP_403_FORBIDDEN)

# @api_view(['GET', 'POST'])
# def comment_list_or_create(request, board_id):
#     token = request.data.get('headers').get('Authorization')
#     user_token = checkuser(token)
#     user = get_object_or_404(get_user_model(), id=user_token)
#     board = get_object_or_404(Board, id=board_id)

#     if request.method == 'GET':
#         comments = board.comment_set.order_by('-id')
#         serializer = CommentListSerializer(comments, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = CommentListSerializer(data=request.data.get("data"))
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(board_id=board, user_id=user)

#             comments = board.comment_set.order_by('-id')
#             serializer = CommentListSerializer(comments, many=True)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['PUT', 'DELETE'])
# def comment_update_or_delete(request, board_id, comment_id):
#     token = request.data.get('headers').get('Authorization')
#     user_id = checkuser(token)
#     user = get_object_or_404(get_user_model(), id=user_id)
#     board = get_object_or_404(Board, id=board_id)
#     comment = get_object_or_404(Comment, id=comment_id)
    
#     if request.method == 'PUT':
#         if user == comment.user:
#             serializer = CommentListSerializer(instance=comment, data=request.data.get("data"))
#             if serializer.is_valid(raise_exception=True):
#                 serializer.save(board=board, user=user)
#                 comments = board.comment_set.order_by('-id')
#                 serializer = CommentListSerializer(comments, many=True)
#                 return Response(serializer.data)
#     elif request.method == 'DELETE':
#         if user == comment.user:
#             comment.delete()
#             comments = board.comment_set.order_by('-id')
#             serializer = CommentListSerializer(comments, many=True)
#             return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
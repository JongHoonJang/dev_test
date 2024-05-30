from django.db.models import F
from backend.common import checkuser
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Board, Counting
from .serializers import BoardListSerializer, BoardDetailSerializer
from django.db.models.aggregates import Max

# Create your views here.
@api_view(["GET"])
def board_list(request):
    if request.method == "GET":
        boards = Board.objects.order_by('group_order','order_id')
        
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(["POST"])
def board_create(request):
    board = Board()
    token = request.data.get('headers').get('Authorization')
    user_token = checkuser(token)
    user = get_object_or_404(get_user_model(), id=user_token)
    board.title = request.data.get('data').get('title')
    board.content = request.data.get('data').get('content')
    board.user_id = user
    # 새글 작성일 경우
    if request.data.get('no') == -1:
        value = Board.objects.aggregate(max_groupno=Max('group_order'))
        if value["max_groupno"] == None:
            value["max_groupno"] = 0
        board.group_order = value["max_groupno"] + 1
        board.save()
        return Response(status=status.HTTP_200_OK)
    # 답글 작성일 경우 order_id, group_order, depth 설정
    else:
        board2 = Board.objects.get(id=request.data.get('no'))
        # 답글이 작성될 경우, 작성되는 답글의 order_id+1보다 크거나 같은 그룹 내의 이전 게시글의 order_id +1씩 올려주어야 한다.
        Board.objects.filter(order_id__gte=board2.order_id + 1).update(order_id=F('order_id')+1)
        board.group_order = board2.group_order
        board.order_id = board2.order_id + 1
        board.depth = board2.depth + 1
        board.save() 
        return Response(status=status.HTTP_200_OK)
    # if request.method == "POST":
    #     serializer = BoardCreateSerializer(data=board)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(user_id=user)
    #     return Response(status=status.HTTP_201_CREATED)
    
@api_view(["GET", "PUT", "DELETE"])
def board_detail_or_update_or_delete(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == "GET":
        serializer = BoardDetailSerializer(board)
        return Response(serializer.data, status=status.HTTP_200_OK)
    token = request.data.get('headers').get('Authorization')
    user_token = checkuser(token)
    user = get_object_or_404(get_user_model(), id=user_token)
    if request.method == "PUT":
        serializer = BoardDetailSerializer(instance=board, data=request.data.get("data"))
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=user)
        return Response(status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        print(board.user_id.id, user.username, user_token)
        if board.user_id.id == user_token:
            board.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            data = {
                '게시글을 삭제할 수있는 권한이 없습니다.'
            }
            return Response(data,status=status.HTTP_403_FORBIDDEN)

    return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(["GET"])
def get_counting(request, board_id):  
    board = get_object_or_404(Board,id=board_id)
    if 'headers' in request.META.keys():
        token = request.META.get("HTTP_AUTHORIZATION")
        user_token = checkuser(token)
        user = get_object_or_404(get_user_model(), id=user_token)
        if not board.counting.filter(ip=user.username).exists():
           board.counting.create(ip=user.username)  
    else:
        ip = request.META.get('REMOTE_ADDR')
        if not board.counting.filter(ip=ip).exists():
            board.counting.create(ip=ip)

    return Response(status=status.HTTP_200_OK)




# from django.shortcuts import get_object_or_404, render
# from django.contrib.auth import get_user_model
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Board
# from .serializers import BoardCreateSerializer, BoardDetailSerializer


# # Create your views here.
# @api_view(["GET"])
# def board_list(request):
#     if request.method == "GET":

#         boards = Board.objects.order_by("id")
#         serializer = BoardDetailSerializer(boards, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(status=status.HTTP_403_FORBIDDEN)

# @api_view(["POST"])
# def board_create(request):
#     if request.method == "POST":
#         serializer = BoardCreateSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response(status=status.HTTP_201_CREATED)
    
# @api_view(["GET", "PUT", "DELETE"])
# def board_detail_or_update_or_delete(request):
#     board_id = request.data.get("id")
#     borad = get_object_or_404(Board, id=board_id)
    
#     if request.method == "GET":
#         serializer = BoardDetailSerializer(borad)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == "PUT":
#         serializer = BoardDetailSerializer(instance=borad, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response(status=status.HTTP_200_OK)

#     elif request.method == "DELETE":
#         borad.delete()
#         return Response(status=status.HTTP_200_OK)

#     return Response(status=status.HTTP_403_FORBIDDEN)
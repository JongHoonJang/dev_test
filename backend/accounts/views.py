from django.shortcuts import render
from backend.common import checkuser
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from .serializers import (
    UserSignupSerializer
)

@api_view(["POST"])
def login(request):
    print(request.data)
    username=request.data.get("data").get("username")
    password=request.data.get("data").get("password")
    user = get_user_model().objects.get(username=username)
    
    if user is not None and check_password(password, user.password):

        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        data = {
            "refresh": refresh_token,
            "access": access_token,
        }
        return Response(data, status=status.HTTP_200_OK)

    return Response(status=status.HTTP_403_FORBIDDEN)


# 로그아웃
@api_view(["POST"])
def logout(request):
    if request.method == "POST":
        token = request.data.get('headers').get('Authorization')
        user_id = checkuser(token)
        tokens = OutstandingToken.objects.filter(user_id=user_id)
        if tokens is not None:
            for token in tokens:
                t, _ = BlacklistedToken.objects.get_or_create(token=token)
                token.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

# 회원가입 신청
@api_view(["POST"])
def signup(request):
    if request.method == "POST":
        user = UserSignupSerializer(data=request.data.get("data"))
        if user.is_valid(raise_exception=True):
            user.save()
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_403_FORBIDDEN)

        


@api_view(["GET", "PUT", "DELETE"])
def user_detail_or_update_or_delete(request):
    token = request.data.get('headers').get('Authorization')
    user_id = checkuser(token)
    user = get_object_or_404(get_user_model(), id=user_id)
    # 유저 상세정보
    # if request.method == "GET":
    #     serializer = UserDetailSerializer(user)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # 유저 정보 수정
    if request.method == "PUT":
        serializer = UserSignupSerializer(instance=user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)
    # 회원 탈퇴(비활성화)
    elif request.method == "DELETE":
        tokens = OutstandingToken.objects.filter(user_id=user_id)
        if tokens is not None:
            for token in tokens:
                token.delete()
        user.delete()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_403_FORBIDDEN)
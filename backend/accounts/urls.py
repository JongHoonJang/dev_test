from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    path("user/", views.user_detail_or_update_or_delete),
    # JWT 토큰 발행
    path('user/login/', views.login),
    # refresh토큰으로 유저 확인후 access토큰 재발행
    path('user/token/reissuance/', TokenRefreshView.as_view()),

    path("user/logout/", views.logout),
    path("user/signup/", views.signup)
]
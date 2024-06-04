from django.urls import path
from . import views

urlpatterns = [
    path('<int:board_id>/',views.board_detail_or_update_or_delete),
    path('list/', views.board_list),
    path('create/', views.board_create),
    path('counting/<int:board_id>/', views.get_counting)
]
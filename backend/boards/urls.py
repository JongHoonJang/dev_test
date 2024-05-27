from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.board_list),
    path('create/', views.board_create),
    path('<int:board_id>/',views.board_detail_or_update_or_delete),
    #test url
    path('counting/', views.get_counting)
    # path('<int:board_id>/comment/',views.comment_list_or_create),
    # path('<int:board_id>/comment/<int:comment_id>',views.comment_update_or_delete),
]
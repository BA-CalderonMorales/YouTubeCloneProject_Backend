from django.urls import path
from . import views

urlpatterns = [
    path('youtube_app/', views.CommentList.as_view()),
    path('youtube_app/<int:pk>', views.CommentDetail.as_view()),
    path('youtube_app/<int:pk>', views.CommentDetail.as_view(), name="update_likes"),
    path('youtube_app/<int:pk>', views.CommentDetail.as_view(), name="update_dislikes")

]
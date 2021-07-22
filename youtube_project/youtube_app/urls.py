from django.urls import path
from . import views

urlpatterns = [
    path('youtube_app/', views.CommentList.as_view()),
    path('youtube_app/<int:pk>', views.CommentDetail.as_view()),
    path('youtube_app/like/<int:pk>', views.Like.as_view()),
    path('youtube_app/dislike/<int:pk>', views.Dislike.as_view())
]



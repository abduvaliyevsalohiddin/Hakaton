from django.urls import path

from .views import *

urlpatterns = [
    path('comments/', CommentListAPIView.as_view()),
    path('comment_create/', CommentCreateView.as_view()),
    path('like_create/', LikeCreateAPIView.as_view()),

]

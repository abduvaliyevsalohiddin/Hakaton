from django.urls import path

from .views import *

urlpatterns = [
    path('ConnectionCreate/<int:pk>/', ConnectionAPIView.as_view()),

]

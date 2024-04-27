from django.urls import path

from .views import *

urlpatterns = [
    path('category/', CategoryListCreateView.as_view()),
    path('projects/', ProjectAPIView.as_view()),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view()),

]

from django.urls import path

from .views import *

urlpatterns = [
    path('create_connect/', ConnectionCreateAPIView.as_view()),
    path('vacancies/', VacanciesAPIView.as_view())
]

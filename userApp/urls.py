from django.urls import path

from .views import *

urlpatterns = [
    path('register/', ProfilRegistrationView.as_view()),
    path('profil/<int:pk>/', ProfilRetrieveUpdateDestroyView.as_view()),
    path('profile/', ProfileAPIView.as_view()),

]

from django.views.generic import *
from rest_framework.generics import *
from rest_framework.permissions import *
from .serializers import *


class ProfilRegistrationView(CreateAPIView):
    permission_classes = (AllowAny)
    serializer_class = ProfilSerializer
    queryset = Profil.objects.all()


class ProfilRetrieveUpdateDestroyView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated)
    serializer_class = ProfilSerializer
    queryset = Profil.objects.all()

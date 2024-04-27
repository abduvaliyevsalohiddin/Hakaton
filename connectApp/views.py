from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import *

from connectApp.models import Connection
from connectApp.serializers import ConnectionSerializer
from userApp.models import Profil


class ConnectionCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ConnectionSerializer
    queryset = Connection.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            user1=self.request.user
        )

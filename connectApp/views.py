from rest_framework.views import *

from connectApp.serializers import ConnectionSerializer
from userApp.models import Profil


class ConnectionAPIView(APIView):
    def post(self, request, pk):
        data = request.data
        serializer = ConnectionSerializer(data=data)
        if serializer.is_valid():
            serializer.save(
                user1=request.user,
                user2=Profil.objects.get(id=pk)
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

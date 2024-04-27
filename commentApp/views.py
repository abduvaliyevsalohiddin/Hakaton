from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import *

from .models import *
from .serializers import *


class CommentListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="user_id",
                in_=openapi.IN_QUERY,
                description="Filter by User ID",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                name="project_id",
                in_=openapi.IN_QUERY,
                description="Filter by Project ID",
                type=openapi.TYPE_INTEGER,
            )
        ],
    )
    def get(self, request):
        comments = Comment.objects.all()
        user_id = request.query_params.get('user_id')
        project_id = request.query_params.get('project_id')
        if project_id:
            comments = comments.filter(project__id=project_id)
        if user_id:
            comments = comments.filter(project__user__id=user_id)

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class LikeCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )

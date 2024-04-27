from rest_framework.generics import *
from rest_framework.permissions import *
from rest_framework.views import *

from mainApp.serializers import *
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class CategoryListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ProjectAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="price",
                in_=openapi.IN_QUERY,
                description="Filter by Price",
                type=openapi.TYPE_INTEGER,
            ),
        ],
    )
    def get(self, request):
        projects = Project.objects.all()
        price = request.query_params.get('price')
        if price:
            projects = projects.filter(price__gte=float(price))

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user=request.user
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


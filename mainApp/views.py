from rest_framework import filters
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

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    search_description = 'Search by name and description'
    ordering_fields = ['id', 'name']


class ProjectAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="price",
                in_=openapi.IN_QUERY,
                description="Filter by Price",
                type=openapi.TYPE_INTEGER,
            ),
            openapi.Parameter(
                name="category_id",
                in_=openapi.IN_QUERY,
                description="Filter by Category ID",
                type=openapi.TYPE_INTEGER,
            ),
        ],
    )
    def get(self, request):
        projects = Project.objects.all()
        price = request.query_params.get('price')
        category_id = request.query_params.get('category_id')
        if price:
            projects = projects.filter(price__gte=float(price))
        if category_id:
            projects = projects.filter(category=category_id)

        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=ProjectSerializer,
    )
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


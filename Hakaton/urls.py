from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view

from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, )

schema_view = get_schema_view(
    openapi.Info(
        title="Hakaton API",
        default_version='v1',
        description="Test Hakaton API",
        contact=openapi.Contact("Abduvaliyev Salohiddin. Email: abduvaliyevsalohiddin568@gmail.com")
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainapp/', include('mainApp.urls')),
    path('commentapp/', include('commentApp.urls')),
    path('connectapp/', include('connectApp.urls')),
    path('userapp/', include('userApp.urls')),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

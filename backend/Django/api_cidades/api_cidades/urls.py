"""
URL configuration for api_cidades project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from cidades import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'estados', views.EstadoViewSet)
router.register(r'cidades', views.CidadeViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="API Cidades Documentação",
        default_version='v1',
        description="API para Cidades e Estados",
        terms_of_service="https://www.google/politics/terms/",
        contact=openapi.Contact(email="catce.2024111mtds0019@aluno.ifpi.edu.br"),
        license=openapi.License(name="BSB License"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cidades/', include(router.urls)),
    path('cidades/auth/', include('cidades.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
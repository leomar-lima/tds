from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import EstadoViewSet, CidadeViewSet, SignupView, SignupJWTView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'cidades', CidadeViewSet)

estado_router = routers.NestedDefaultRouter(
    router, r'estados', lookup='estado')
estado_router.register(r'cidades', CidadeViewSet, 
                       basename='estado-cidades')

urlpatterns = [
    path('', include(router.urls)),
    path('',include(estado_router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signup-jwt/', SignupJWTView.as_view(), name='signup-jwt'),
    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from rest_framework import viewsets, permissions, generics, parsers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import decorators
from rest_framework_simplejwt.tokens import RefreshToken
from .filters import EstadoFilter, CidadeFilter
from .pagination import CustomPagination

from .models import Estado, Cidade
from .serializers import EstadoSerializer, UploadFotoEstadoSerializer, CidadeSerializer, SignupSerializer

# Viewsets
class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    filterset_class = EstadoFilter
    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticated]

    parser_classes = [parsers.JSONParser, parsers.MultiPartParser]

    def get_serializer_class(self):
        if self.action == ['upload_foto']:
            return UploadFotoEstadoSerializer
        return EstadoSerializer

    @decorators.action(url_path='upload_foto', detail=True, methods=['put'])
    def upload_foto(self, request, pk):
        estado = Estado.objects.get(pk=pk)
        if not estado:
            return Response({"detail": "Estado não encontrado."}, status=404)
        serializer = UploadFotoEstadoSerializer(
            instance=estado, data=request.data
        )
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(EstadoSerializer(serializer.instance).data)
class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    filterset_class = CidadeFilter
    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cidade.objects.filter(dono=self.request.user)

    def perform_create(self, serializer):
        serializer.save(dono=self.request.user)

    

# Signup View usando GenericAPIView
class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.get_object()
        token = Token.objects.create(user=user)
        return Response({'token': token.key})

# Signup View usando JWT
class SignupJWTView(generics.CreateAPIView):
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = self.get_object()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

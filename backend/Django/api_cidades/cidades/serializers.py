from rest_framework import serializers
from .models import Estado, Cidade
from django.contrib.auth.models import User

class CidadeSerializer(serializers.ModelSerializer):
    dono = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cidade
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    cidades = CidadeSerializer(many=True, read_only=True)
    foto = serializers.ImageField(read_only=True)

    class Meta:
        model = Estado
        fields = '__all__'

class UploadFotoEstadoSerializer(serializers.ModelSerializer):
    foto = serializers.ImageField(required=True)

    class Meta:
        model = Estado
        fields = ['foto']

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

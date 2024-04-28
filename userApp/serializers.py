from rest_framework import serializers
from .models import *


class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = '__all__'

    def create(self, validated_data):
        return Profil.objects.create_user(**validated_data)

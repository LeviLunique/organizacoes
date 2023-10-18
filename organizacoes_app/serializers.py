from rest_framework import serializers
from .models import Organizacao

class OrganizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacao
        fields = ['id', 'nome', 'idade', 'endereco', 'telefone']
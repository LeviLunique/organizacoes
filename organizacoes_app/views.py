from django.shortcuts import render
from rest_framework import viewsets
from .models import Organizacao
from .serializers import OrganizacaoSerializer

class OrganizacaoViewSet(viewsets.ModelViewSet):
    queryset = Organizacao.objects.all()
    serializer_class = OrganizacaoSerializer

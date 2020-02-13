from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Dados
from .serializers import DadosSerializer

class DadosList(generics.ListAPIView):
   queryset = Dados.objects.all()
   serializer_class = DadosSerializer
   permission_classes = ()
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import DataTable
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class DataTableAPIView(ModelViewSet):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']
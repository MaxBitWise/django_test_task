from django.shortcuts import render
from rest_framework import generics
from .models import Date, DataTable
from .serializers import DataTableSerializer


class DataTableAPIView(generics.ListAPIView):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer
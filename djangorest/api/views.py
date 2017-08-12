from django.shortcuts import render
from rest_framework import generics
from .serializers import CarSerializer
from django_filters import rest_framework as filters
from .models import Car

class CreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('model', 'make', 'age')

    def perform_create(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

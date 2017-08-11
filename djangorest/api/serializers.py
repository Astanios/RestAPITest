from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'name', 'brand', 'color', 'automatic', 'insured', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

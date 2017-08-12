from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'model', 'make', 'color', 'age', 'insured', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

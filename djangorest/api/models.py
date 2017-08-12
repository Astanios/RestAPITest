from django.db import models
from django_filters import rest_framework as filters
import datetime
YEAR_CHOICES = []
for r in range(1900, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r,r))

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=255, blank=False, unique=True)
    make = models.CharField(max_length=255, blank=False, unique=True)
    color = models.CharField(max_length=255, blank=False, unique=True)
    age = models.IntegerField(('age'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    insured = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    pass

    def __str__(self):
        return "{}".format(self.name)

class CarFilter(filters.FilterSet):
    class meta:
        model = Car
        fields = ('model','make','age')

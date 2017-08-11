from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    brand = models.CharField(max_length=255, blank=False, unique=True)
    color = models.CharField(max_length=255, blank=False, unique=True)
    automatic = models.BooleanField(default=False)
    insured = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    pass

    def __str__(self):
        return "{}".format(self.name)

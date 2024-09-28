from django.db import models
from eventorganizer.models.events import Events

class Customers(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    location = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    event = models.ForeignKey(Events, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
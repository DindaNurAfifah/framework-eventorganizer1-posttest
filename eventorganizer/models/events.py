from django.db import models
from eventorganizer.models.organizers import Organizers

class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    organizer = models.ForeignKey(Organizers, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/')  
    
    def __str__(self):
        return self.title
    
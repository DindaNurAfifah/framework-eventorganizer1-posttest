from django import forms
from .models import Events

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['title', 'description', 'category', 'theme', 'organizer', 'image']
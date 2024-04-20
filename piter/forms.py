from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone

from .models import Event

class EventForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    class Meta:
        model = Event

        fields = ['title', 'description', 'start_date', 'end_date', 'location', 'attendees', 'organizer']
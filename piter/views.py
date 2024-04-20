from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets

from .forms import EventForm
from .models import Event
from .serializers import EventSerializer

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_create')
    else:
        form = EventForm()
    return render(request, 'event_create.html', {'form': form})

def event_update(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_update', event_id=event.id) # Предполагается, что у вас есть URL с именем 'event_list'
    else:
        form = EventForm(instance=event)

    return render(request, 'event_update.html', {'form': form})

def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        event.delete()
        return redirect('events_list') # Предполагается, что у вас есть URL с именем 'event_list'

    return render(request, 'event_delete.html', {'event': event})
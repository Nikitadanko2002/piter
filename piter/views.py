import requests
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


def show_categories(request):
    # Получаем данные о категориях
    categories_url = 'https://spb-afisha.gate.petersburg.ru/kg/external/afisha/categories'
    response = requests.get(categories_url)
    json_response = response.json()
    categories = json_response['data']
    return render(request, 'categories.html', {'categories': categories})

def show_events_by_category(request, category_slug):
    events_url = f'https://spb-afisha.gate.petersburg.ru/kg/external/afisha/events?lat=59.939016&lng=30.31588&radius=5&categories={category_slug}&fields=categories%2Cdescription%2Cid%2Cplace%2Ctitle%2Cage_restriction%2Cis_free%2Cimages&expand=images%2Cplace%2Clocation%2Cdates%2Cparticipants&page=1&count=10'
    response = requests.get(events_url)
    json_response = response.json()
    events = json_response.get('data', [])  # Получаем значение для ключа 'data' или пустой список, если ключ отсутствует
    return render(request, 'events.html', {'events': events})


def show_sport_categories(request):
    categories_url = 'https://egs.gate.petersburg.ru/egs/sportgrounds/?season=%D0%9B%D0%B5%D1%82%D0%BE&page=1&count=10'
    response = requests.get(categories_url)
    json_response = response.json()

    categories = []
    for item in json_response['data']:
        place = item['place']
        categories.extend(place['categories'].split(', '))

    categories = list(set(categories))  # Удаляем повторяющиеся категории и преобразуем в список
    print(categories)
    return render(request, 'sport_categories.html', {'categories': categories})


def show_sports_by_category(request, category_name):
    events_url = f'https://egs.gate.petersburg.ru/egs/sportgrounds/?types={category_name}&season=%D0%9B%D0%B5%D1%82%D0%BE&page=1&count=20'
    response = requests.get(events_url)
    json_response = response.json()

    sports = []
    for item in json_response['data']:
        place = item['place']
        if category_name in place['categories'].split(', '):
            sports.append(place)

    return render(request, 'sports_by_category.html', {'category_name': category_name, 'sports': sports})



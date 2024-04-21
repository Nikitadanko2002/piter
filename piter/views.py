import requests
from django.shortcuts import render, redirect, get_object_or_404


from .forms import EventForm, GroupForm
from .models import Event, Group, User
from .serializers import EventSerializer

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
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


def show_categories_event(request):
    # Получаем данные о категориях
    categories_url = 'https://spb-afisha.gate.petersburg.ru/kg/external/afisha/categories'
    response = requests.get(categories_url)
    json_response = response.json()
    categories = json_response['data']
    return render(request, 'Site3/index.html', {'categories': categories})


import json
from django.http import JsonResponse
import requests


def show_categories(request):
    # Получаем данные о категориях
    categories_url = 'https://spb-afisha.gate.petersburg.ru/kg/external/afisha/categories'
    response = requests.get(categories_url)
    json_response = response.json()
    categories = json_response['data']

    # Возвращаем JSON-ответ с данными о категориях
    return JsonResponse(categories, safe=False)


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


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_list.html', {'groups': groups})

def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'group_create.html', {'form': form})

def group_update(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'group_update.html', {'form': form})

def group_delete(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    return render(request, 'group_delete.html', {'group': group})


def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'Site3/index.html', {'user': user})

def eventtt(request):
    return render(request, 'Site3/typeEvent.html')

def friendss(request):
    return render(request, 'Site3/friends.html')


def mainn(request):
    return render(request, 'Site3/index.html')


def user_friends(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        friends = user.friends.all()
        friend_list = [{'id': friend.id, 'avatar':friend.avatar.url, 'first_name': friend.first_name, 'second_name': friend.second_name} for friend in friends]
        return JsonResponse({'friends': friend_list})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)


def all_users(request):
    users = User.objects.all()
    return render(request, 'site3/friends.html', {'users': users})

def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'site3/profile.html', {'user': user})
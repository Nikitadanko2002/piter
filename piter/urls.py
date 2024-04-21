from django.urls import path

from piter import views
from piter.jsonparse import *

urlpatterns = [
    path('events_list/', views.event_list, name='events_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('event/update/<int:event_id>/', views.event_update, name='event_update'),
    path('event/delete/<int:event_id>/', views.event_delete, name='event_delete'),
    path('import-json/', import_data_from_url, name='import_data_from_url'),
    path('categories/', views.show_categories, name='categories'),
    path('events/<slug:category_slug>/', views.show_events_by_category, name='events_by_category'),
    path('sport_categories/', views.show_sport_categories, name='categories'),
    path('sport/<str:category_name>/', views.show_sports_by_category, name='sports_by_category'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/create/', views.group_create, name='group_create'),
    path('groups/<int:group_id>/update/', views.group_update, name='group_update'),
    path('groups/<int:group_id>/delete/', views.group_delete, name='group_delete'),
    path('main/', views.show_categories_event, name='categories'),
    path('main/<int:user_id>/', views.user_profile, name='user_profile'),
    path('events/', views.eventtt, name='events'),
    path('mainn/', views.mainn, name='mainn'),
    path('fr/', views.friendss, name='friends'),
    path('user/<int:user_id>/friends/', views.user_friends, name='user_friends'),


]
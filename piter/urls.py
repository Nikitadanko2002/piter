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

]
from django.urls import path

from piter import views
from piter.jsonparse import import_data_from_url

urlpatterns = [
    path('events_list/', views.event_list, name='events_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('event/update/<int:event_id>/', views.event_update, name='event_update'),
    path('event/delete/<int:event_id>/', views.event_delete, name='event_delete'),
    path('import-json/', import_data_from_url, name='import_data_from_url'),
]
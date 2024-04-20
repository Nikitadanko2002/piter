from django.urls import path, include
from rest_framework.routers import DefaultRouter

from piter import views


urlpatterns = [
    path('events_list/', views.event_list, name='events_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('event/update/<int:event_id>/', views.event_update, name='event_update'),
    path('event/delete/<int:event_id>/', views.event_delete, name='event_delete'),
]
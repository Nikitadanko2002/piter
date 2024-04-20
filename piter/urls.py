from django.contrib import admin
from django.urls import path

from piter.views import fetch_and_save_data

urlpatterns = [
    path('admin/', admin.site.urls),
]


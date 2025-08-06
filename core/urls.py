# core/urls.py

from django.contrib import admin
from django.urls import path, include  # include is required to import app urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # connect home.urls to root URL
]

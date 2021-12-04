from django.contrib import admin
from django.urls import path, include

from .views import *


urlpatterns = [
    path('', Vini.as_view(), name='vini'),
]

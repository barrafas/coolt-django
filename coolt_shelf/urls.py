"""coolt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('404', error_404, name='404'),
    path('about', about, name='about'),
    path('animes', animes, name='animes'),
    path('books', books, name='books'),
    path('games', games, name='games'),
    path('home', home, name='home'),
    path('movies', movies, name='movies'),
    path('profile', profile, name='profile'),
    path('series', series, name='series'),
    path('work', work, name='work'),
]

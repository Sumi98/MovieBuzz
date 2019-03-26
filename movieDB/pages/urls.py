from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('movie/', views.movie, name = 'movie'),
    path('director/', views.director, name = 'director'),
    path('actor/', views.actor, name = 'actor'),
]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('movie/', views.movie, name = 'movie'),
    path('director/', views.director, name = 'director'),
    path('actor/', views.actor, name = 'actor'),
    path('prediction/', views.prediction, name = 'prediction'),
    path('recommendation/', views.recommendation, name = 'recommendation'),
    path('insert_data/', views.insert_data, name = 'insert_data'),
    path('insert_data_submission/', views.insert_data_submission, name = 'insert_data_submission')
]
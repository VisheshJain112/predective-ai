from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('extraction', views.extraction, name='extraction'),
   

    
]

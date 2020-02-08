from django.contrib import admin
from django.urls import path
from .views import home, projects, references

urlpatterns = [
    path('', home, name='home'),
    path('projects/', projects, name='projects'),
    path('references/', references, name="references")
]

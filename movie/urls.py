from django.urls import path
from django.shortcuts import render

from .views import homepage

urlpatterns = [
    path('', homepage)
]

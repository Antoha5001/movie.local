from django.urls import path
from django.shortcuts import render

from .views import homepage, Homepage, HomepageDetail

urlpatterns = [
    path('<slug:slug>/', HomepageDetail.as_view(), name='home_detail'),
    path('', Homepage.as_view(), name='home'),
]

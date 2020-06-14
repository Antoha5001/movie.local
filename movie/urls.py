from django.urls import path
from django.shortcuts import render

from .views import homepage, Homepage, HomepageDetail, PostComment

urlpatterns = [
    path('<slug:slug>/', HomepageDetail.as_view(), name='home_detail'),
    path('comment/<int:pk>/', PostComment.as_view(), name='post_comment'),
    path('', Homepage.as_view(), name='home'),
]

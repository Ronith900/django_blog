from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(),name='blog-home'),
    path('about/', views.About.as_view(),name='blog-about'),
    path('create/', views.Create.as_view(),name='blog-create'),
]

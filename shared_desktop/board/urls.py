"""board URL Configuration."""
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index),
    path('rules/', views.rules_list),
    path('rules/<pk>/', views.rules_detail),
]

"""board URL Configuration."""
from django.urls import path
from . import views 

app_name = 'rules'

urlpatterns = [
    path('', views.index, name='rules'),
    path('rules/', views.rules_list, name='rule'),
    path('rules/<pk>/', views.rules_detail),
]

"""board URL configuration."""
from django.urls import path

from . import views

app_name = "prog"

urlpatterns = [
    path("", views.prog, name="prog"),
    path("passport/equipment_layout/", views.equipment_layout, name="equipment_layout"),
]

"""board URL configuration."""
from django.urls import path

from . import views

app_name = "tools"

urlpatterns = [
    path("", views.tools, name="tools"),
    path("tools/calculate_cycle/", views.calculate_cycle, name="calculate_cycle"),
]

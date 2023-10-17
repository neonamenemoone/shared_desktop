"""board URL configuration."""
from django.urls import path

from . import views

app_name = "tools"

urlpatterns = [
    path("", views.tools, name="tools"),
    path("calculate_cycle/", views.calculate_cycle, name="calculate_cycle"),
    path("technical_coordination/", views.technical_coordination, name="technical_coordination"),
    path("phase_control/", views.phase_control, name="phase_control"),
]

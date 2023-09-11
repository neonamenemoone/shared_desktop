"""shared_desktop URL Configuration."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('board.urls')),
    path('admin/', admin.site.urls),
]

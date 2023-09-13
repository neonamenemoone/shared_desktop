"""shared desktop URL configuration."""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('board.urls')),
    path('prog/', include('prog.urls')),
    path('tools/', include('tools.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/notes/', include('ideasrecording.urls')),
    path('api/', include('djoser.urls')),
    path('api/', include('users.urls')),
]

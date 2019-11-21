from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('history.urls')),
    path('index/', include('history.urls')),
    path('history/', include('history.urls')),
    path('add/', include('history.urls')),
    path('admin/', admin.site.urls),
]

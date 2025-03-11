from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_academia.urls')),
    path('app_academia/', include('app_academia.urls')),
]

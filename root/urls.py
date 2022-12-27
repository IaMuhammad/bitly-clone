from django.contrib import admin
from django.urls import path, include

def divide_zero():
    return 1/0

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
    path('error/', divide_zero),
]

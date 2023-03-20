from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('katri.urls')),
    path('admin/', admin.site.urls),
]
from django.contrib import admin
from django.urls import path

from .views import index as i

urlpatterns = [
    path('',i,name="jaane be."),
]
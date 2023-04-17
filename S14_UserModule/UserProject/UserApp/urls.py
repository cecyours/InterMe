"""UserProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signin_user,name="sign-in-user"),
    path('signup',views.signup_user,name="sign-up-user"),
    path('logout',views.logout_,name="logout-user"),
    path('test',views.user_test,name="user-test"),
    path('dashboard',views.user_dashboard,name="user-dashboard"),
    path('result',views.result,name="user-result"),
    path('list',views.get_list,name="get-list"),
    path('home',views.home,name="home-page"),
    path('demo',views.demo,name="demo"),

    
]

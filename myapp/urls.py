"""RealEstate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from .import views

urlpatterns = [

    path('', views.index, name="index"),
    path('login', views.login, name="login"),
    path('registration', views.registration, name="registration"),

    path('register', views.register, name="register"),

    path('login_check', views.login_check, name="login_check"),
    path('logout', views.logout, name="logout"),
    path('propertys', views.propertys, name="propertys"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('Upload_property', views.Upload_property, name="Upload_property"),
    path('Your_property', views.Your_property, name="Your_property"),
    #path('property_upload', views.property_upload, name="property_upload"),
    path('property_details', views.property_details, name="property_details"),
    path('search_property', views.search_property, name="search_property"),
    path('search', views.search, name="search"),
    # path('usercheck', views.usercheck, name="usercheck"),


    path('demo', views.demo, name="demo"),

]

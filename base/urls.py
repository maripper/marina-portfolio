"""proect5o URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
import base.views as views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
    path('', views.home,name='home'),
    path('welcome/', views.welcome,name='welcome'),
    path('start/', views.start,name='start'),
    path('software_development/', views.software_development,name='software_development'),
    path('research/', views.research,name='research'),
    path('artistic/', views.artistic,name='artistic'),
    # path(
    # "favicon.ico",
    # RedirectView.as_view(url="https://res.cloudinary.com/hhx0pttis/image/upload/v1667924921/samples/favicon_ssi6ij.ico"),
    # )

]

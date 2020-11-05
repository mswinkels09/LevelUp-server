"""levelup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from levelupapi.views import register_user, login_user
from levelupapi.views import Games, GameTypes, Events, Profile


### Your new request_handler.py###

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'gametypes', GameTypes, 'gametype')
#(r=patternmatch'what string client is looking for'
# Class that you are looking for, 
# 'descriptive name')
router.register(r'games', Games, 'game')
router.register(r'events', Events, 'event')
router.register(r'profile', Profile, 'profile')

urlpatterns = [
    path('', include(router.urls)),
    #http://localhost:8000/register
    path('register', register_user),
    #http://localhost:8000/login
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', base_page, name='base_page'),
    path('profile', profile_user, name='profile_user'),
    
]


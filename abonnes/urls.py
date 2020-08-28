from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import (
    home,
    login,
    user_login,
    add_profile

)

app_name = 'params'

urlpatterns = [
    path('home', home, name='home'),
    path('add_profile', add_profile, name='add_profile'),
    path('', user_login, name='login'),
]
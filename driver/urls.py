from django.contrib import admin
from django.urls import path, include  
from . import views


# urls.py

from .views import driver_dashboard, edit_driver_profile, driver_home

urlpatterns = [
    # Your other URL patterns
    path('driver_dashboard/', driver_dashboard, name='driver_dashboard'),
    path('edit_driver_profile/', edit_driver_profile, name='edit_driver_profile'),
    path('driver_home/', driver_home, name='driver_home'),
    path('driver_profile/', views.driver_profile, name='driver_profile'), 
    path('driver_panel/', views.driver_panel, name='driver_panel'),
    path('create_driver_profile/', views.create_driver_profile, name='create_driver_profile'),


]

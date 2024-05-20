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
    path('available_ambulances/', views.available_ambulances, name='available_ambulances'),
    path('hire_request/<int:ambulance_id>/', views.hire_request, name='hire_request'),
    path('ambulance_detail/<int:ambulance_id>/', views.ambulance_detail, name='ambulance_detail'),
    path('driver_hire_requests/', views.driver_hire_requests, name='driver_hire_requests'),
    path('driver_messages/', views.driver_messages, name='driver_messages'),
    path('update_hire_request/<int:request_id>/', views.update_hire_request, name='update_hire_request'),
]
from django.urls import path, include  # new
from . import views
urlpatterns = [
    path("/", include("django.contrib.auth.urls")), 
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),
    path('user_profile/', views.user_profile, name='user_profile'),
    #path('driver_profile/', views.driver_profile, name='driver_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]

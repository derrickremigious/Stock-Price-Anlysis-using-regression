"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.Landing_1, name='Landing_1'),
    path('Home_4/', views.Home_4, name='Home_4'),
    path('Domain/', views.Domain, name='Domain'),
    
    path('Tcs_Report/', views.Tcs_Report, name='Tcs_Report'),
    path('Accenture_Report/', views.Accenture_Report, name='Accenture_Report'),

    path('show_tcs_predictions/', views.show_tcs_predictions, name='show_tcs_predictions'),
    path('show_accenture_predictions/', views.show_accenture_predictions, name='show_accenture_predictions'),
    

    path('Deploy_8/', views.Deploy_8, name='Deploy_8'),
    path('Deploy_9/', views.Deploy_9, name='Deploy_9'),
   
    path('Login_2/', views.Login_2, name='Login_2'),
    path('Register_3/', views.Register_3, name='Register_3'),
    path('logout/', views.logout, name='logout'),
    
]

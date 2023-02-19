# Page Url du site

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("create_account/", views.create_account), # page of sign up
    path("homepage/", views.homepage), # page of login
]
            
            

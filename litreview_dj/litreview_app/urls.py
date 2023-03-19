# Page Url du site

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path("create_account/", views.create_account, name='create_account'), # page of sign up
    # path("homepage/", views.homepage, name='homepage'),# page of login\    
    path('login/', views.user_login, name='login'), #Ajout Livre
    # path("feed/", views.feed, name='feed') # Page de flux d'actualité
    ]
            
            

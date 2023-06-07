# Page Url du site

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [  
    path('login/', views.user_login, name='login'), #Page de connection
    path('login/', auth_views.LoginView.as_view(), name='login'), #certification de la connexion
    path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.user_register, name='register'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('create_ticket_and_review/', views.create_ticket_and_review, name='create_ticket_and_review'),
    path('posts/', views.posts, name='posts'),
    path('update_ticket/<int:ticket_id>', views.update_ticket, name='update_ticket'),
    ]
            
            
 
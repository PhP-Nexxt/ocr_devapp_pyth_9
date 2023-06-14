# Page Url du site

from django.urls import path
from . import views as views_ #Redirection
from django.contrib.auth import views as auth_views

urlpatterns = [  
    path('login/', views_.user_login, name='login'), #Page de connection
    path('login/', auth_views.LoginView.as_view(), name='login'), #certification de la connexion
    path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name='logout'),
    path('dashboard/', views_.dashboard, name='dashboard'),
    path('register/', views_.user_register, name='register'),
    path('create_ticket/', views_.create_ticket, name='create_ticket'),#Le premier parametre peut etre modifié(Seo par Ex)
    path('create_ticket_and_review/', views_.create_ticket_and_review, name='create_ticket_and_review'),
    path('posts/', views_.posts, name='posts'),
    path('update_ticket/<int:ticket_id>', views_.update_ticket, name='update_ticket'),
    path('create_review/<int:ticket_id>', views_.create_review, name='create_review'),
    path('update_review/<int:review_id>', views_.update_review, name='update_review'),#Parametre1=url/Parametre2=nom fonction/Parametre3=nom template html
    path('delete_ticket/<int:ticket_id>', views_.delete_ticket, name='delete_ticket'),
    path('delete_review/<int:review_id>', views_.delete_review, name='delete_review'),
    ]
            
            

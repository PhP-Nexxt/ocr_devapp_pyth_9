# Avec Django la vue recoit les requetes http et renvoie une reponse inteigible par la navigateur, 
# la vue realise toutes les actions necessaires à la requete et fait appel au model (bd) ou au template (affichage) selon le besoins

from itertools import chain
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout 
from django.db.models import CharField, Value
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm, SignupForm, ReviewForm
from .forms import LoginForm
from .models import UserFollows
from .models import Review
from .utils import get_users_viewable_tickets, get_users_viewable_reviews


def user_login(request): #Formulaire de connection
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')  # Redirige vers la vue associée à l'URL 'dashboard'
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'litreview_app/login.html', {'form': form})

   
@login_required
def dashboard(request):
    tickets = Ticket.objects.all().order_by('-id') # Récupérer les tickets et les trier par ordre décroissant d'ID
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    
    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    
    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )

    context = {
        'section': 'dashboard', 
        'posts' : posts,
    }
    
    return render(request, 'litreview_app/dashboard.html', context) 


@login_required
def create_ticket(request): #création du ticket dans le dashboard
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()
            messages.success(request, 'Ticket créé avec succès.')
            return redirect('dashboard')
    else:
        form = TicketForm()
    return render(request, 'litreview_app/create_ticket.html', {'form': form})

    
def user_register(request): # Formulaire de création de compte
    form = SignupForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Connecter l'utilisateur après l'inscription
            login(request, user)
            return redirect('dashboard') # Redirige vers la vue associée à l'URL 'dashboard'
        else:
            return HttpResponse('Registration failed')
    else:
        form = UserCreationForm()
    return render(request, 'litreview_app/register.html', {'form': form})


def logout_view(request): 
    logout(request)
    return redirect('litreview_app/login.html')


@login_required #Création d'une critique pas en reponse a un ticket(cad creation du ticket puis de la critique)
def create_ticket_and_review(request):
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST, request.FILES)
        if ticket_form.is_valid() and review_form.is_valid():
            new_ticket = ticket_form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()

            new_review = review_form.save(commit=False)
            new_review.ticket = new_ticket  # Assuming your Review model has a foreign key to Ticket model
            new_review.user = request.user
            new_review.save()

            messages.success(request, 'Ticket and review created successfully.')
            return redirect('dashboard')

    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    return render(request, 'litreview_app/create_ticket_and_review.html', {'ticket_form': ticket_form, 'review_form': review_form})

@login_required
def posts(request): #mes postes uniquements
    tickets = Ticket.objects.all().order_by('-id') # Récupérer les tickets et les trier par ordre décroissant d'ID
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    
    reviews = Review.objects.all()
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    
    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )
    context = {
        'section': 'dashboard', 
        'posts' : posts,
    }
    return render(request, 'litreview_app/posts.html', context) 

login_required
def update_ticket(request, ticket_id): #Modification du ticket dashboard
    ticket = Ticket.objects.get(id=ticket_id) #recuperation du ticket id pour modification
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()
            messages.success(request, 'Ticket modifié avec succès.')
            return redirect('dashboard')
    else:
        form = TicketForm(instance=ticket) #On passe l'instance correspondant au Ticket à modifier afin de récuperer les informations
    return render(request, 'litreview_app/update_ticket.html', {'form': form})

@login_required #Création d'une critique en reponse a un ticket
def create_review(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id) #Recuperation du ticket id pour ajout de critique
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.ticket = ticket  # Assuming your Review model has a foreign key to Ticket model
            new_review.user = request.user
            new_review.save()

            messages.success(request, 'Review created successfully.')
            return redirect('dashboard')

    else:
        review_form = ReviewForm()
    
    #La clé est ce que je veux utiliser à l'interieur de mon template html 
    # et la valeur c'est le contenu 
    context = {
        'review_form': review_form,
        'ticket': ticket
    }
    return render(request, 'litreview_app/create_review.html', context)




""" (reprendre apres les critiques)
@login_required
def follow_user(request, user_id): #Formulaire de suivi d'autre user 
    user_to_follow = get_object_or_404(User, id=user_id)
    follow, created = UserFollows.objects.get_or_create(user=request.user, followed_user=user_to_follow)

    if created:
        # Utilisateur a commencé à suivre
        pass
    else:
        # Utilisateur suit déjà
        pass

    return redirect('profile', user_id=user_id)
"""

#Fonction pour ajout de review




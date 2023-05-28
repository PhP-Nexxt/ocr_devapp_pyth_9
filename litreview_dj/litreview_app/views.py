# Avec Django la vue recoit les requetes http et renvoie une reponse inteigible par la navigateur, 
# la vue realise toutes les actions necessaires à la requete et fait appel au model (bd) ou au template (affichage) selon le besoins

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout 
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm, SignupForm, ReviewForm
from .models import UserFollows
from .models import Review




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
    reviews = Review.objects.all() # récupérer toutes les critiques

    context = {
        'section': 'dashboard', 
        'tickets': tickets,
        'reviews': reviews
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


@login_required #(En cours)création d'une critique pas en reponse a un ticket(cad creation du ticket puis de la critique)
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




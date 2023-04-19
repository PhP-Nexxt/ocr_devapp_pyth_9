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
from .forms import TicketForm



#Formulaire de connection
def user_login(request):
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

   
@login_required #Decorateur secure connexion 
def dashboard(request):
    tickets = Ticket.objects.all().order_by('-id') # Récupérer les tickets et les trier par ordre décroissant d'ID
    
    #return render(request,'litreview_app/dashboard.html',{'section': 'dashboard'}) #affichage dashboard
    return render(request,'litreview_app/dashboard.html', {'section': 'dashboard', 'tickets': tickets}) #affichage dashboard = des tickets


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

    


 
# Formulaire de création de compte
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Connecter l'utilisateur après l'inscription
            login(request, user)
            return redirect('dashboard')
            #return render(request, 'litreview_app/dashboard.html')  # Redirige vers la vue associée à l'URL 'dashboard'
        else:
            return HttpResponse('Registration failed')
    else:
        form = UserCreationForm()
    return render(request, 'litreview_app/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('litreview_app/login.html')




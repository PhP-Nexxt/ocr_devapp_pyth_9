# Avec Django la vue est le controleur

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout 
from litreview_app.forms import SignupForm


#fonction Creation compte
def create_account(request):
    form = SignupForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'litreview_app/create_account.html', {'form': form})

def login(request):
    pass
    
    
    
    
def homepage(request):
    return render(request, "litreview_app/homepage.html")

#fonctionLogin
def login_litreview(username, password):
    from django.contrib.auth import authenticate
    user = authenticate(username=username, password=password)
    if user is not None:
        return True
    else:
        return False

#Ici 2 fonctions python pour se connecter et creer un compte avec les url associés ci-dessus pour semaine prochaine

def feed(request):
    return render(request, "litreview_app/feed.html")
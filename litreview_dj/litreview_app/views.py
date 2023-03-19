# Avec Django la vue recoit les requetes http et renvoie une reponse inteigible par la navigateur, 
# la vue realise toutes les actions necessaires à la requete et fait appel au model (bd) ou au template (affichage) selon le besoins

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout 
from .forms import LoginForm

"""
def homepage(request):
    return render(request, "litreview_app/homepage.html")
"""

#Ajout du livre
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
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'litreview_app/login.html', {'form': form})
 


"""
#fonction Creation compte et redirection vers la page login
def create_account(request):
    form = SignupForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, 'litreview_app/create_account.html', {'form': form})

    

def login(username, password): # Pour next week creer la fonction login et rediriger l'utilisateur vers le feed
    user = authenticate(username=username, password=password)
    if user is not None:
        return True 
        #return HttpResponse('litreview_app/feed')
    else:
        return False
    

# Puis rediriger sur le flux (reprendre les etape et voir docuemntation Django pour login et redirection)
    
    
def feed(request):
    return render(request, "litreview_app/feed.html"
"""


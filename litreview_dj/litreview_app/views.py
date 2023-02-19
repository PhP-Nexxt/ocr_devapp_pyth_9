# Avec Django la vue est le controleur

from django.http import HttpResponse
from django.shortcuts import render

def create_account(request):
    return render(request, "litreview_app/create_account.html") #Url local a taper dans le navigateur (Redirection)
    
def homepage(request):
    return render(request, "litreview_app/homepage.html")

#Ici 2 fonctions pythpn pour se connecter et creer un compte avec les url associés ci-dessus pour semaine prochaine

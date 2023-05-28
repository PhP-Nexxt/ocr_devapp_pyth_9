# Ici on fait le lien entre html et Python

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Ticket
from .models import UserFollows
from .models import Review


class SignupForm(UserCreationForm): #Ici on importe le formulaire de creation de compte
    
    class Meta(UserCreationForm.Meta): # Les modifications sur les champ se font ici et pas sur l'Html
        model = get_user_model()
        fields = 'username', 'password1', 'password2'
      

class LoginForm(forms.Form): #Formulaire de connexion
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class TicketForm(forms.ModelForm): #Formulaire creation ticket
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image',)
        
class ReviewForm(forms.ModelForm): #Formulaire de creation de Critique pas en reponse a un ticket (en cours)
    RATING_CHOICES = [(i, i) for i in range(1, 6)] #Affichage Radio Button
    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)
    
    class Meta:
        model = Review
        fields = ('headline', 'body', 'rating',)
        
        
"""class ReviewForm(forms.ModelForm): #Formulaire de creation de Critique  en reponse a un ticket 
    class Meta:
        model = Review
        fields = ('headline', 'body', 'rating', 'ticket')
"""
        
""" (a reprendre apres les tickets)
class UserFollows(forms.ModelForm): #Formulaire de suivi autre utilisateurs (Mentorat 21/05)
    model = UserFollows
    fields = ('a definir')
"""
# Ici on fait le lien entre html et Python

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


"""
class SignupForm(UserCreationForm): #Ici on importe le formulaire de creation de compte
    
    class Meta(UserCreationForm.Meta): # Les modifications sur les champ se font ici et pas sur l'Html
        model = get_user_model()
        fields = 'username', 'password1', 'password2'
        """

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


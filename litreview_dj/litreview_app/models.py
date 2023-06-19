from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.

#Le modele effectue les requetes dans la base de donnée
#Il utilise un ORM 
# Ici on code les formulaires





class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to='tickets/') #Ajout du repertoire pour stocker les images
    #(indique que les images seront stockées dans un sous-répertoire nommé "tickets" à l'intérieur du répertoire MEDIA_ROOT)

class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following') #Celui qui est suivi
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by') #Celui qui suit
    
    class Meta: #Abonnement Unique
        unique_together = ('user', 'followed_user')
       
class Review(models.Model):
    rating = models.PositiveSmallIntegerField(max_length=1024, validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    #CASCADE = si on supprime le ticket, ca supprime également le review associé(Else on mettra PROTECT)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    
    

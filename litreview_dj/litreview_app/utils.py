# Fichier de fonctions annexes

from django.db.models import Q  # Objet "Queryset" permet d'écrire des conditions
from litreview_app.models import Review, Ticket, UserFollows


def get_users_viewable_reviews(user):
    myfollows = UserFollows.objects.filter(
        followed_user=user
    )  # Filtre Les gens a qui je suis abonné
    myfollows_user = [
        myfollow.user for myfollow in myfollows
    ]  # Iteration sur les gens que je suis (liste)
    reviews = Review.objects.filter(
        Q(user__in=myfollows_user) | Q(user=user) | Q(ticket__user=user)  # User suivi(Q1)Review j'ai crées(Q2)Si je auteur du ticket associé a la review (Q3)
        # Récupérer toutes les critiques
    )
    return reviews


def get_users_viewable_tickets(user):
    myfollows = UserFollows.objects.filter(
        followed_user=user
    )  # Filtres Les gens a qui je suis abonné
    myfollows_user = [
        myfollow.user for myfollow in myfollows
    ]  # Iteration sur les gens que je suis
    tickets = Ticket.objects.filter(
        Q(user__in=myfollows_user) | Q(user=user)
    )  # # récupérer toutes les tickets 1Les personne que je suis (Q1) et 2les tickets que j'ai crées(Q2)
    return tickets

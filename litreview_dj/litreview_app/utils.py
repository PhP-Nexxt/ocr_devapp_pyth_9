# Fichier de fonctions annexes

from litreview_app.models import Review, Ticket



def get_users_viewable_reviews(user):
    reviews = Review.objects.all() # récupérer toutes les critiques
    return reviews

def get_users_viewable_tickets(user):
    tickets = Ticket.objects.all() # recuperer les tickets
    return tickets
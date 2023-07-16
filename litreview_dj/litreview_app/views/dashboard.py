from itertools import chain
from django.shortcuts import render
from django.db.models import CharField, Value
from django.contrib.auth.decorators import login_required
from litreview_app.models import Ticket
from litreview_app.models import Review
from litreview_app.utils import get_users_viewable_tickets, get_users_viewable_reviews


@login_required
def dashboard(request):
    tickets = get_users_viewable_tickets(
        request.user
    )  # Récupérer les tickets et les trier par ordre décroissant d'ID
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )

    context = {
        "section": "dashboard",
        "posts": posts,
    }

    return render(request, "litreview_app/dashboard.html", context)


@login_required
def posts(request):  # mes postes uniquements # --> Erreur on recupere tous les tickets  à reprendre juste les miens <--

    tickets = Ticket.objects.filter(user=request.user).order_by("-id")
    # tickets = Ticket.objects.all().order_by( "-id")
    # Récupérer les tickets et les trier par ordre décroissant d'ID
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))

    reviews = Review.objects.filter(user=request.user).order_by("-id")
    # reviews = Review.objects.all() # --> Idem ici <--
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))

    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )
    context = {
        "section": "dashboard",
        "posts": posts,
    }
    return render(request, "litreview_app/posts.html", context)

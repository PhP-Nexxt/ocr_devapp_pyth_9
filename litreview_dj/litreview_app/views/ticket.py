from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from litreview_app.models import Ticket
from litreview_app.forms import TicketForm, ReviewForm


@login_required
def create_ticket(request):  # création du ticket dans le dashboard
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()
            messages.success(request, "Ticket créé avec succès.")
            return redirect("dashboard")
    else:
        form = TicketForm()
    return render(request, "litreview_app/create_ticket.html", {"form": form})


@login_required  # Création d'une critique pas en reponse a un ticket(cad creation du ticket puis de la critique)
def create_ticket_and_review(request):
    if request.method == "POST":
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST, request.FILES)
        if ticket_form.is_valid() and review_form.is_valid():
            new_ticket = ticket_form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()

            new_review = review_form.save(commit=False)
            new_review.ticket = new_ticket  # Assuming your Review model has a foreign key to Ticket model
            new_review.user = request.user
            new_review.save()

            messages.success(request, "Ticket and review created successfully.")
            return redirect("dashboard")

    else:
        ticket_form = TicketForm()
        review_form = ReviewForm()

    return render(
        request,
        "litreview_app/create_ticket_and_review.html",
        {"ticket_form": ticket_form, "review_form": review_form},
    )


login_required
def update_ticket(request, ticket_id):  # Modification du ticket dashboard
    ticket = Ticket.objects.get(
        id=ticket_id
    )  # recuperation du ticket id pour modification
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()
            messages.success(request, "Ticket modifié avec succès.")
            return redirect("dashboard")
    else:
        form = TicketForm(
            instance=ticket
        )  # On passe l'instance correspondant au Ticket à modifier afin de récuperer les informations
    return render(request, "litreview_app/update_ticket.html", {"form": form})


@login_required  # Suppression d'un ticket
def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(
        id=ticket_id
    )  # Recuperation du ticket id pour suppression
    ticket.delete()
    return redirect("posts")

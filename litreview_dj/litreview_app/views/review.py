
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from litreview_app.models import Ticket
from litreview_app.forms import ReviewForm
from litreview_app.models import Review

@login_required #Création d'une critique en reponse a un ticket
def create_review(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id) #Recuperation du ticket id pour ajout de critique
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.ticket = ticket  # Assuming your Review model has a foreign key to Ticket model
            new_review.user = request.user
            new_review.save()

            messages.success(request, 'Review created successfully.')
            return redirect('dashboard')
    else:
        review_form = ReviewForm()
    
    #La clé est ce que je veux utiliser à l'interieur de mon template html 
    # et la valeur c'est le contenu 
    context = {
        'review_form': review_form,
        'ticket': ticket
    }
    return render(request, 'litreview_app/create_review.html', context)

@login_required #Modification d'une critique en reponse a un ticket
def update_review(request, review_id):
    review = Review.objects.get(id=review_id)#Recuperation de la critique id pour ajout de critique
    ticket = review.ticket 
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.ticket = ticket  # Assuming your Review model has a foreign key to Ticket model
            new_review.user = request.user
            new_review.save()

            messages.success(request, 'Review updated successfully')
            return redirect('dashboard')

    else:
        review_form = ReviewForm(instance=review)
    
    #La clé est ce que je veux utiliser à l'interieur de mon template html 
    # et la valeur c'est le contenu 
    context = {
        'review_form': review_form,
        'ticket': ticket
    }
    return render(request, 'litreview_app/update_review.html', context)

@login_required #Suppression d'un ticket
def delete_review(request, review_id):
    review = Review.objects.get(id=review_id) #Recuperation de la critique id pour suppression
    review.delete()
    return redirect('posts')

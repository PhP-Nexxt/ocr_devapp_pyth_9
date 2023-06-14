from itertools import chain
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout 
from django.db.models import CharField, Value
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from litreview_app.models import Ticket
from litreview_app.forms import TicketForm, SignupForm, ReviewForm
from litreview_app.forms import LoginForm
from litreview_app.models import UserFollows
from litreview_app.models import Review
from litreview_app.utils import get_users_viewable_tickets, get_users_viewable_reviews


def user_login(request): #Formulaire de connection
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
                    return redirect('dashboard')  # Redirige vers la vue associée à l'URL 'dashboard'
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'litreview_app/login.html', {'form': form})

   
@login_required
def dashboard(request):
    tickets = Ticket.objects.all().order_by('-id') # Récupérer les tickets et les trier par ordre décroissant d'ID
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    
    reviews = get_users_viewable_reviews(request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    
    # combine and sort the two types of posts
    posts = sorted(
        chain(reviews, tickets), 
        key=lambda post: post.time_created, 
        reverse=True
    )

    context = {
        'section': 'dashboard', 
        'posts' : posts,
    }
    
    return render(request, 'litreview_app/dashboard.html', context) 
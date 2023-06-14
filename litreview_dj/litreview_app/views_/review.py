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
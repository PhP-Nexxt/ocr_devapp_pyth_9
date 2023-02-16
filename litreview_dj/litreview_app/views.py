
from django.http import HttpResponse
from django.shortcuts import render

def create_account(request):
    return render(request, "litreview_app/create_account.html")
    
def homepage(request):
    return render(request, "litreview_app/homepage.html")

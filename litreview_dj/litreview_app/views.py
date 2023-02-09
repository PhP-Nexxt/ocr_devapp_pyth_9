
from django.http import HttpResponse
from django.shortcuts import render # Initial Code 

def hello(request):
    return HttpResponse("<h1>Hello Django!</h1>")
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, you at the Zed soccer site.")

def details(request, team = "kaunda FC"):
    response = "You are looking at the page of %s football club"
    return HttpResponse(response % team)

def newscorner(request):
    introduction = "Latest news in League"
    return HttpResponse(introduction)

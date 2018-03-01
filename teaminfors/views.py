from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'test_dict'
'''
def index(request):
    test_string = "Zambia football test"
    context = {'test': test_string,}
    return render(request,'teaminfors/index.html', context)

def details(request, team = "kaunda FC"):
    response = "You are looking at the page of %s football club"
    return HttpResponse(response % team)

def newscorner(request):
    introduction = "Latest news in League"
    return HttpResponse(introduction)
'''
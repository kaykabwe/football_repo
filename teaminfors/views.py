from django.shortcuts import render 
from django.views import generic
from django.http import HttpResponse

# views for the forms to be rendered
from django.http import HttpResponseRedirect

from .forms import NameForm

# Create your views here.
'''
class IndexView(generic.ListView):
    template_name = 'teaminfors/index.html'
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
    introduction = "Latest news in League. Thanks!!"
    return HttpResponse(introduction)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
   
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('./thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    
    return render(request, 'teaminfors/name.html', {'form': form})
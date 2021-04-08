from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Files
from .forms import SearchForm

def index(request): 
    context = {
        'filtered_entries': Files.objects.all()[:5],
    }
    return render(request, 'search/index.html', context)

    # template = loader.get_template('search/index.html')
    # context = {
    #     'filtered_entries': Files.objects.all()[:5],
    # }
    # return HttpResponse(template.render(context, request))

def search(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':        
        # Create a form instance and populate it with data from the request (binding):
        form = SearchForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            #process the data in form.cleaned_data as required           

            #redirect to a new URL:
            return HttpResponseRedirect(reverse('index')) #HttpResponseRedirect(reverse('search/index'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = SearchForm()

    context = {
        'form': form,
    }

    return render(request, 'search/index_form.html', context)
    



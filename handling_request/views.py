from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def view1(request):
    print('... hi from view ...') # middleware test
    return render( request, 'handling_request/options.html')

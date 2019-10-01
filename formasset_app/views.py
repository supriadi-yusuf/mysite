from django.shortcuts import render

# Create your views here.

from .forms import StudentForm

def fill(request):
    form = StudentForm()
    return render( request, 'formasset_app/formasset-1.html', { 'form':form })

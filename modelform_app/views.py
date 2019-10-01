from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from .forms import AuthorForm, AuthorForm2, AuthorForm3, ArticleForm

def show_override_field(request):
    form1 = AuthorForm()
    form2 = AuthorForm2()

    return render(request, 'modelform_app/show-override.html', {
        'form1' : form1,
        'form2' : form2
    })

def show_override_field2(request):
    if request.method == 'POST':
        form3 = AuthorForm3(request.POST)
        if form3.is_valid():
            return HttpResponse('Ok...')
    else:
        form3 = AuthorForm3()

    return render(request, 'modelform_app/show-override-2.html', {
        'form' : form3,
    })

def show_override_field3(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            return HttpResponse('Ok...')
    else:
        form = ArticleForm()

    return render(request, 'modelform_app/show-override-2.html', {
        'form' : form,
    })

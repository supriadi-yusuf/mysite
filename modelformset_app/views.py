from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelformset_factory
import datetime

from modelform_app.models import Author

# Create your views here.

def show_modelformset(request):
    AuthorFormSet = modelformset_factory( Author, fields='__all__', extra=2)
    data = [
        {'title':'MRS', 'name':'cucu', 'birth_date':datetime.date(1991,10,5)},
        {'title':'MR', 'name':'rusdi', 'birth_date':datetime.date(1980,6,5)},
        {'title':'MRS', 'name':'endang astuti', 'birth_date':datetime.date(1985,10,29)},
    ]
    if request.method == 'POST' :
        formset = AuthorFormSet(request.POST, request.FILES, initial=data)
        #print(request.POST)
        #print(formset.is_valid())
        #if formset.is_valid():
        #    objects = formset.save()
        #    return HttpResponse('ok')
    else :
        formset = AuthorFormSet(initial=data)

    return render(request, 'modelformset_app/show_formset.html', {'formset':formset})

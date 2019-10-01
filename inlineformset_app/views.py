from django.shortcuts import render
from django.forms import inlineformset_factory

# Create your views here.
from .models import Author, Book

def show_inline_formset(request):
    BookFormSet = inlineformset_factory( Author, Book,
        fields=('title',), # fields of book
        extra=2)
    author = Author.objects.get(name='supriadi')
    if request.method == 'POST':
        formset = BookFormSet(request.POST, request.FILES, instance=author)
        if formset.is_valid():
            formset.save()
    else:
        formset = BookFormSet(instance=author)

    return render( request, 'inlineformset_app/show_inline_formset.html',
                   {'formset':formset})

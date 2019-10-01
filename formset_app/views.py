from django.shortcuts import render
from django.forms import formset_factory
from django.http import HttpResponse

from .forms import ArticleForm, BaseArticleFormSet

# Create your views here.

def register_articles(request):

    ArticleFormset = formset_factory( ArticleForm, formset=BaseArticleFormSet, \
    extra=3, can_delete=True)

    if request.method == 'POST':

        new_post = request.POST.copy()

        for key,val in new_post.items():
            print((key,val))

        new_post['form-TOTAL_FORMS'] = '3'
        new_post['form-INITIAL_FORMS'] = '0'
        new_post['form-MAX_NUM_FORMS'] = ''

        articleFormset = ArticleFormset(new_post)
        if articleFormset.is_valid():
            return HttpResponse('test')
    else:
        articleFormset = ArticleFormset()

    return render(request, 'formset_app/articles.html', {'formset':articleFormset})

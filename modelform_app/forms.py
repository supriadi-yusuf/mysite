from django import forms
from . import models

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['name', 'title', 'birth_date']
        #fields = '__all__' # we can simply use it

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['name', 'authors']

"""
# Two forms above are similar to these forms :
class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100)
    title = forms.CharField(
        max_length=3,
        widget = forms.Select(choices=TITLE_CHOICES)
    )
    birth_date = forms.DateField(required=False)

class BookForm(forms.Form):
    name = forms.CharField(max_length=100)
    authors = forms.ModelMultipleChoiceField(queryset=Author.objects.all())
"""

class PartialAuthorForm(forms.ModelForm):
      class Meta:
            model = models.Author
            exclude = ['title', 'birth_date'] # exclude some fields

class JournalForm(forms.ModelForm):
    class Meta:
        model = models.Journal
        fields = '__all__'

class AuthorForm2(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ('name', 'title', 'birth_date')
        widgets = {
            'name' : forms.Textarea(attrs={'cols':50, 'rows':10}), # field name that we want to override
        }

from django.utils.translation import ugettext_lazy as _
class AuthorForm3(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ('name', 'title', 'birth_date')
        labels = {
            'name' : _("Writer"),
        }
        help_texts = {
            'name' : _("Some useful help text."),
        }
        error_messages = {
            'name' : {
                'max_length' : _("This writer's name is too long."),
            },
        }

class AuthorForm4(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ('name', 'title')

    def clean_name(self): # custom validation : what's effect?
        print("clean_name is executed ...")

class ArticleForm(forms.ModelForm):
    headline = forms.CharField(
         max_length=200,
         required=False,
         help_text='Use puns liberally')

    class Meta:
        model = models.Article
        fields = ('headline', 'content')

class BaseAuthorFormSet(forms.BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = models.Author.objects.filter(name__istartswith = 's')

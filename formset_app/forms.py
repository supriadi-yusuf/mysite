from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

class MyArticleForm(ArticleForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args,**kwargs)

    def get_user(self):
        return self.user

class BaseArticleFormSet(forms.BaseFormSet):

    def add_fields(self, form, index):
        super().add_fields( form, index)
        form.fields['new_field']=forms.CharField()

    def clean(self):
        """check that no two articles have the same title"""
        if any(self.errors):
            # do not bother validating the formset unless each form is valid on its own
            return

        titles=[]
        for form in self.forms:
            title = form.cleaned_data['title']
            if title in titles:
                raise forms.ValidationError("Articles in a set must have distinct titles.")

            titles.append(title)

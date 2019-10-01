from django.forms import BaseModelFormSet

class AuthorBaseFormSet(BaseModelFormSet):
    def clean(self):
        super().clean()

        print('override clean() method')

        for form in self.forms:
            # form.cleaned_data['...']
            pass

class AuthorBaseFormSet2(BaseModelFormSet):
    def clean(self):
        super().clean()

        print('override clean() method 2')

        for form in self.forms:
            name = form.cleaned_data['name'].upper()
            form.cleaned_data['name'] = name

            #update instance value
            form.instance.name = name

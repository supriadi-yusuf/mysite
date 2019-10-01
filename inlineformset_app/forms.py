from django.forms import BaseInlineFormSet

class BaseAuthorinlineFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()

        print("base author inline form set override")
        for form in self.forms:
            print(form.cleaned_data)

from django import forms
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # print(self.cleaned_data)
        pass

def comment_validation(value):
    if len(value) < 4:
        raise ValidationError('comment is too short')

class CommentForm(forms.Form):
    comment = forms.CharField(validators=[comment_validation])

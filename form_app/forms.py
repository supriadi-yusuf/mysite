from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField( label='Your name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField( label='Email subject :', max_length=100)
    message = forms.CharField( label='Your message :', widget=forms.Textarea)
    sender = forms.EmailField( label='Your email address :')
    cc_myself = forms.BooleanField( label='Cc yourself ?', required=False)
    secret = forms.CharField(widget=forms.HiddenInput, initial='1234')

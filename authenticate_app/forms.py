from django import forms

class LoginForm(forms.Form):
    dest_url = forms.CharField(widget=forms.HiddenInput)
    username = forms.CharField(label='user name', max_length=20)
    password = forms.CharField(label='password', widget=forms.PasswordInput,max_length=20)

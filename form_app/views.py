from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import NameForm, ContactForm

# Create your views here.

def get_name(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request :
        form = NameForm(request.POST)
        if form.is_valid():
            # process data in form.cleaned_data[...] as required
            # ....
            # redirect to a new URL
            return HttpResponseRedirect('')

    else:
        form = NameForm()

    return render( request, 'form_app/name.html', {'form':form,})

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipient = ['superriyadi@yahoo.com']
            if cc_myself:
                recipient.append(sender)

            send_mail(subject,message,sender,recipient)

            return HttpResponseRedirect('')
    else:
        form = ContactForm()

    #return render(request, 'form_app/contact.html', {'form':form})
    #return render(request, 'form_app/contact_manually.html', {'form':form})
    return render(request, 'form_app/contact_manually-2.html', {'form':form})
    #return render(request, 'form_app/contact-2.html', {'form':form})
    #return render(request, 'form_app/contact-display-errors.html', {'form':form})
    #return render(request, 'form_app/include-form.html', {'form':form})

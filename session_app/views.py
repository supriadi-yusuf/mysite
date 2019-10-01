from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_session(request):
    print('.... Session ....')
    print(dir(request.session))
    return HttpResponse('Thank you')

def set_session(request):
    request.session['name'] = 'supriadi'
    request.session['address'] = 'jakarta'
    return HttpResponse('Thanks')

def get_session(request):
    name = request.session['name']
    address = request.session['address']
    return HttpResponse("name = %s, address = %s" % (name,address))

def delete_session(request):
    del request.session['name']
    del request.session['address']
    return HttpResponse("sessions deleted")

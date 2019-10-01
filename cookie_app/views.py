from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_cookie(request):
    print('.... Cookies ....')
    print(dir(request.COOKIES))
    return HttpResponse('Thank you')

def set_cookie(request):
    response = HttpResponse('Thanks')
    response.set_cookie('name','supriadi')
    response.set_signed_cookie('address','jakarta') 
    return response

def get_cookie(request):
    name = request.COOKIES['name']
    address = request.get_signed_cookie('address')
    return HttpResponse("name = %s, address = %s" % (name,address))

def delete_cookie(request):
    response = HttpResponse("cookie deleted")
    response.delete_cookie('name')
    response.delete_cookie('address')
    return response

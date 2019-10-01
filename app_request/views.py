from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list( request, namespace_status=None, *prm, **prm2):
    return render( request, template_name='app_request/list.html', context = {'status' : namespace_status,})

def detail( request, namespace_status=None, *prm, **prm2):
    return render( request, template_name='app_request/detail.html', context = {'status' : namespace_status,})

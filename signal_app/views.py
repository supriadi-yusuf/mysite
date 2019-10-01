from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .signals import get_supri_signal
from . import receivers # register receivers by importing module defining them

# Create your views here.

class SignalView(View):
    def get(self, *args, **kwargs):
        get_supri_signal().send(sender=self.__class__, name='supri', age=30)
        # do something
        #get_supri_signal().disconnect()
        return HttpResponse('ok')

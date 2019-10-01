from django.shortcuts import render
from django.http import HttpResponse
import logging

# Create your views here.

logger = logging.getLogger(__name__)
#logger = logging.getLogger('logging_app.views')

def view1(request):
    #print(dir(logger))
    logger.info('access view 1')
    logger.error('this is error')
    return HttpResponse('logging ... 1')

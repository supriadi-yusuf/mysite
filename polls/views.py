from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from django.template import loader

from . import models

# Create your views here.

def index(request):
    latest_questions = models.Question.objects.order_by('-pub_date')[:5]
    context = {
    'latest_questions' : latest_questions,
    }
    return render( request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id) 
    return render(request ,'polls/detail.html', {'question' : question})

def results(request, question_id):
    response = "You're looking at result of question %s."
    return HttpResponse( response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting at question %s" % question_id)

def mhs(request, nama, nim):
    return HttpResponse("nama : %s<br>nim : %s" % (nama, nim))

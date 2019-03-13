from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.

def index(request):
    latest_questions = models.Question.objects.order_by('-pub_date')[:5]
    output = ", ".join([q.question_text for q in latest_questions])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at result of question %s."
    return HttpResponse( response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting at question %s" % question_id)

def mhs(request, nama, nim):
    return HttpResponse("nama : %s<br>nim : %s" % (nama, nim))

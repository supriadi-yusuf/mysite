from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.template import loader
from django.urls import reverse
from django.db.models import F

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
    question = get_object_or_404(models.Question, pk=question_id)
    return render(request,"polls/results.html", {
        "question" : question,
    })

def vote(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question' : question,
            'error_message' : "You didn't select any choice"
        })
    else:
        selected_choice.votes = F('votes') + 1 # solving race condition problem
        selected_choice.save()
        # always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a user
        # hits the back button
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def mhs(request, nama, nim):
    return HttpResponse("nama : %s<br>nim : %s" % (nama, nim))

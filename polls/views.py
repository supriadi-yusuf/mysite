from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.template import loader
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

from . import models

# Create your views here.

class IndexView(generic.ListView):
    # default template_name : <app_name>/<model_name>_list.html
    template_name = "polls/index.html"
    context_object_name = "latest_questions"

    def get_queryset(self):
        """
        returns the last five future questions
        """
        return models.Question.objects.exclude(
          choice__id = None
        ).filter(
            pub_date__lte = timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = models.Question
    # default template_name : <app_name>/<model_name>_detail.html
    template_name = "polls/detail.html"

    def get_queryset(self):
        return super().get_queryset().filter(pub_date__lte = timezone.now()
        ).order_by('-pub_date')

class ResultView(generic.DetailView):
    model = models.Question
    #  default template_name : <app_name>/<model_name>_detail.html
    template_name = "polls/results.html"

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

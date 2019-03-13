from django.conf.urls import url

from . import views

app_name = "polls" #namespace url name

urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(r'^specifics/(?P<question_id>\d+)/$', views.detail, name="detail"),
  url(r'^(?P<question_id>\d+)/results/$', views.results, name="results"),
  url(r'^(?P<question_id>\d+)/vote/$', views.vote, name="vote"),
  url(r'^(?P<nama>\w+)/(?P<nim>\d+)/mhs/$', views.mhs, name="mhs"),
]

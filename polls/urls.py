from django.conf.urls import url

from . import views

app_name = "polls" #namespace url name

urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name="index"),
  url(r'^specifics/(?P<pk>\d+)/$', views.DetailView.as_view(), name="detail"),
  url(r'^(?P<pk>\d+)/results/$', views.ResultView.as_view(), name="results"),
  url(r'^(?P<question_id>\d+)/vote/$', views.vote, name="vote"),
  url(r'^(?P<nama>\w+)/(?P<nim>\d+)/mhs/$', views.mhs, name="mhs"),
]

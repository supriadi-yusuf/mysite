from django.conf.urls import url, include

from . import views

app_name = 'my_app' # applicaton namespace

extrapatterns = [
  url(r'^$', views.list, name='list'),
  url(r'^detail/$', views.detail, name='detail'),
]

urlpatterns = [
  url( r'^$', # url pattern
       views.list, # view function
       name='list' # url name
       ),
  url(r'^detail/$', views.detail, name='detail'),
  url(r'^extra/', include( extrapatterns, namespace='extra'), {'namespace_status':'extra'})
]

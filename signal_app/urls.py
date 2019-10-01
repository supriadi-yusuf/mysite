from django.conf.urls import url

from . import views

urlpatterns = [
    url( r'^signal/$', views.SignalView.as_view()), 
]

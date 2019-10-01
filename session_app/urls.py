from django.conf.urls import url

from . import views

urlpatterns = [
    url( r'^view/$', views.view_session),
    url( r'^set/$', views.set_session),
    url( r'^get/$', views.get_session),
    url( r'^delete/$', views.delete_session),
]

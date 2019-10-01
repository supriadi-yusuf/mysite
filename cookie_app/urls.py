from django.conf.urls import url

from . import views

urlpatterns = [
    url('^view/$', views.view_cookie),
    url('^set/$', views.set_cookie),
    url('^get/$', views.get_cookie),
    url('^delete/$', views.delete_cookie),
]

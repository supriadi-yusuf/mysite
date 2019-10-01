from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^override/$', views.show_override_field),
    url(r'^override-2/$', views.show_override_field2),
    url(r'^override-3/$', views.show_override_field3),
]

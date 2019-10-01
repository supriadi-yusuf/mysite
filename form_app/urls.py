from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^get_name/$', views.get_name),
    url(r'^contact/$',views.contact)
]

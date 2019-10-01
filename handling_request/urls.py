from django.conf.urls import url, include

from . import views
urlpatterns = [
  url(r'^$', views.view1, name='main-menu'),
  url(r'^staff/', include( 'app_request.urls',
                           namespace='staff' # instance namespace
                         ), {'namespace_status':'staff'}),
  url(r'^default/', include( 'app_request.urls',
                             namespace='my_app' # default namespace (instance namespace = application namespace)
                           ), {'namespace_status':'default'}),
  url(r'^nested/', include( 'app_request.urls',
                               namespace='nested' # instance namespace
                          ), {'namespace_status':'nested'}),

]

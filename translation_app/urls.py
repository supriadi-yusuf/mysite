from django.conf.urls import url, include

from . import views

app_name = 'translation-app'

urlpatterns = [
  url(r'^translation-1/$', views.TranslationView1.as_view(), name='translation-1'), # ptyhon code
  url(r'^translation-2/$', views.TranslationView2.as_view(), name='translation-2'), # template code
  url(r'^change-language/(?P<language_code>\w{2})/$', views.ChangeLanguageView.as_view(), name='change-language'),

]

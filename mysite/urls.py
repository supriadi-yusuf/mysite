"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    url(r'^request/', include('handling_request.urls')),
    url(r'^form/', include('form_app.urls')),
    url(r'^formset/', include('formset_app.urls')),
    url(r'^cookie/', include('cookie_app.urls')),
    url(r'^session/', include('session_app.urls')),
    url(r'^modelform/', include('modelform_app.urls')),
    url(r'^modelformset/', include('modelformset_app.urls')),
    url(r'^inlineformset/', include('inlineformset_app.urls')),
    url(r'^formasset/', include('formasset_app.urls')),
    url(r'^class-view/', include('class_view_app.urls')),
    url(r'^authenticate-app/', include('authenticate_app.urls')),
    url(r'^translation-app/', include('translation_app.urls')),
    url(r'^signal-app/', include('signal_app.urls')),
    url(r'^logging-app/', include('logging_app.urls')),
]

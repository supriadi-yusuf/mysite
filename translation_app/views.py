from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils import translation
from django.utils.translation import ugettext as _
from django.conf import settings

# Create your views here.

class TranslationView1(View):
    def get(self, request):
        text = _('Selamat datang di situs kami') # mark this string as translatable
        return HttpResponse(text)

class TranslationView2(View):
    def get(self, request):#     translation_app/translation-2.html
        return render( request, 'translation_app/translation-2.html')

class ChangeLanguageView(View):
    def get(self, request, language_code='id'):

        # check if language is supported
        if not language_code in [lang[0] for lang in settings.LANGUAGES]:
            raise Exception(_('bahasa tidak didukung'))

        if language_code != translation.get_language():
            translation.activate(language_code) # switch active language
            response = TranslationView1.as_view()(request)

            ## make active language persistent by updating session
            #request.session[translation.LANGUAGE_SESSION_KEY] = language_code
            
            # we can also make active language persistent by updating cookie
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language_code)


        else:
            response = TranslationView1.as_view()(request)

        return response

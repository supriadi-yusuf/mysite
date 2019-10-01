from django.utils import translation
from django.conf import settings

class TranslationMiddleware:

  def __init__( self, get_response):
    # one-time configuration and initialization.
    self.__get_response = get_response

  def __call__( self, request):
    # code to be executed for each request before
    # the view (and later middleware) are called.

    # since 'en' will be first time active language
    # we need to change this
    # if active language has been swithed we will give clue in cookie

    if settings.LANGUAGE_COOKIE_NAME in request.COOKIES:
        pass
    else:
        translation.activate(settings.LANGUAGE_CODE)

    response = self.__get_response( request)

    # code to be executed for each request/response after
    # the view is called.

    if settings.LANGUAGE_COOKIE_NAME in request.COOKIES:
        pass
    else:
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, translation.get_language())

    return response

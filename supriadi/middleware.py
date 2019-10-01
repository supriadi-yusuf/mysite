class SimpleMiddleware:

  def __init__( self, get_response):
    # one-time configuration and initialization.
    print('... SimpleMiddleware object init ...')
    self.__get_response = get_response

  def __call__( self, request):
    # code to be executed for each request before
    # the view (and later middleware) are called.

    print('... welcome to SimpleMiddleware object ...')

    response = self.__get_response( request)

    # code to be executed for each request/response after
    # the view is called.

    print('... have a nice day by SimpleMiddleware object ...')

    return response


def simple_middleware(get_response):
    # one-time configuration and initialization.
    print('... simple_middleware function init ...')

    def middleware(request):
        # code to executed for each request before
        # the view (and later middleware) are called.

        print('... welcome to simple_middleware function ...')

        response = get_response(request)

        # code to be executed for each request/response after
        # the view is called

        print('... have a nice day by simple_middleware function ...')

        return response

    return middleware

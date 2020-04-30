# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-
#
from wsgiref.simple_server import make_server


# Every WSGI application must have an application object - a callable
# object that accepts two arguments. For that purpose, we're going to
# use a function (note that you're not limited to a function, you can
# use a class for example). The first argument passed to the function
# is a dictionary containing CGI-style environment variables and the
# second variable is the callable object.


class AppClass:

    def __init__(self, environ=None, start_response=None):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/plain; charset=utf-8')]
        self.start(status, response_headers)
        page = '<h1>Hello world!<h1>'.encode()
        yield page


hello_world_app = AppClass

with make_server('', 8000, hello_world_app) as httpd:
    print("Serving on port 8000...")

    # Serve until process is killed
    httpd.serve_forever()

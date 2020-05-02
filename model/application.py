# Класс WSGI приложения
import os
import wsgiref
from wsgiref.util import FileWrapper
from wsgiref import headers,util
from io import StringIO
import mimetypes


import wsgiref


class AppClass(object):

    def __init__(self, environ=None, start_response=None):
        self.environ = environ
        self.start = start_response

    def __iter__(self):
        status = '200 OK'
        url = self.get_url()
        fn = self.get_file(url)
        typ = os.path.join(url, self.environ['PATH_INFO'][1:])
        typ_in = None
        if typ == 'home/':
            typ_in = 'text/html'

        elif typ == 'open.js/':
            typ_in = 'application/javascript'

        elif typ == 'open.js/':
            typ_in = 'application/javascript '

        elif typ == 'open.css/':
            typ_in = 'text/css'

        elif typ == '':
            typ_in = 'text/plain'

        print(' this is path info ' + typ)
        response_headers = [('Content-type', typ_in + ';charset=utf-8') ]
        self.start(status, response_headers)
        #url = self.get_url()
        print(url)
        if url == "":
            page = '<h1>Index<h1>'.encode()
            yield page
        elif url == 'home':
            line = ['<h1>heello<h1>\n</h1>', '<p>world\n</p>']
            with open(fn) as file:
                array = [row.strip() for row in file]

            for j in array:
                yield j.encode()
        elif url == 'open.js':
            fn = 'open.js'
            with open(fn) as file:
                array = [row.strip() for row in file]

            for j in array:
                yield j.encode()

        elif url == 'open.css':
            fn = 'open.css'
            with open(fn) as file:
                array = [row.strip() for row in file]

            for j in array:
                yield j.encode()


    def get_url(self):
        urls = util.shift_path_info(self.environ)
        print(urls)
        return urls

    def get_file(self, path = None):

        fn = os.path.join(path, self.environ['PATH_INFO'][1:])
        if '.' not in fn.split(os.path.sep)[-1]:
            fn = os.path.join('home.html')
        return  fn


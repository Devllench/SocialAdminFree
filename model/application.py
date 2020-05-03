# Класс WSGI приложения
import datetime
import os
from wsgiref import util

from model.response_body_class import ResponseBodyClass
from model.response_headers_class import ResponseHeadersClass
from model.status_codes_class import StatusCodeClass


class AppClass(object):
    # опрежедение класса
    def __init__(self, environ=None, start_response=None):
        # окружение приложения
        self.environ = environ
        # обьект для формирования запроса
        self.start = start_response
        self.status_codes = StatusCodeClass()
        self.response_headers = ResponseHeadersClass()
        self.response_body = ResponseBodyClass()

    # вызов обьекта класса во время запроса.
    def __iter__(self):
        # ! Клас обработки запроса входящего
        url_request = util.shift_path_info(self.environ)
        print(str(datetime.datetime.now()) + '...1% get url:  :' + url_request)
        # !
        # Классы обработки ответа на запроса
        # указываем status code и response_headers
        status_code = self.status_codes.status_ok
        response_headers = self.response_headers.create_response_headers(url_patch=url_request)
        self.start(status_code, response_headers)

        if url_request == 'testcl':
            fn = os.path.join('home.html')
            response_body = self.response_body.create_string_body(file_patch=fn)
            yield from response_body
        elif url_request == 'home':
            fn = os.path.join('home.html')
            response_body = self.response_body.create_string_body(file_patch=fn)
            yield from response_body
        elif url_request == 'open.css':
            fn = os.path.join('open.css')
            response_body = self.response_body.create_string_body(file_patch=fn)
            yield from response_body
        elif url_request == 'open.js':
            fn = os.path.join('open.js')
            response_body = self.response_body.create_string_body(file_patch=fn)
            yield from response_body
        elif url_request == '':
            response_body = self.response_body.string_body_hello
            yield response_body
        else:
            response_body = self.response_body.string_body_no_found
            yield response_body


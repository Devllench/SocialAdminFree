# Класс WSGI приложения
from wsgiref import util

from model.response_body_class import ResponseBodyClass
from model.response_headers_class import ResponseHeadersClass
from model.status_codes_class import StatusCodeClass
from model.request_date_class import RequestClintClass


class AppClass(object):
    # опрежедение класса
    def __init__(self, environ=None, start_response=None):
        # окружение приложения
        self.environ = environ
        # обьект для формирования ответа
        self.start = start_response
        self.status_codes = StatusCodeClass()
        self.response_headers = ResponseHeadersClass()
        self.response_body = ResponseBodyClass()
        # обекты для получения информации из запроса
        self.request_date = RequestClintClass()

    # вызов обьекта класса во время запроса.
    def __iter__(self):
        # ! Класc обработки запроса входящего
        self.request_date.url_path_info = util.shift_path_info(self.environ)
        # !
        # Формирования ответа на запроса
        # указываем status code и response_headers
        status_code = self.status_codes.status_ok
        response_headers = self.response_headers.create_response_headers(url_patch=self.request_date.url_path_info)
        self.start(status_code, response_headers)
        response_body = self.response_body.create_string_body(file_patch=self.request_date.route())
        yield from response_body

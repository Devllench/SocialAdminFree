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
        self.response_body = ResponseBodyClass()
        # обекты для получения информации из запроса
        self.request_date = RequestClintClass()

    # вызов обьекта класса во время запроса.
    def __iter__(self):
        # ! Класc обработки запроса входящего
        self.request_date.url_path_info = util.shift_path_info(self.environ)
        self.start(self.request_date.route().status_code, self.request_date.get_headers())
        response_body = self.response_body.create_string_body(file_patch=self.request_date.route().file_request)
        yield from response_body


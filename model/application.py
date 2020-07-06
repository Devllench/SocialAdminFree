# Класс WSGI приложения
from wsgiref import util
import wsgiref
from model.request_date_class import RequestClintClass


class AppClass(object):
    # опрежедение класса
    def __init__(self, environ=None, start_response=None):
        # окружение приложения
        self.environ = environ
        # обьект для формирования ответа
        self.start = start_response
        # обекты для получения информации из запроса
        self.request_date = RequestClintClass()

    # вызов обьекта класса во время запроса.
    def __iter__(self):
        self.request_date.url_path_info = util.shift_path_info(self.environ)
        self.start(self.request_date.route().status_code, self.request_date.get_headers())
        print(self.start)
        yield from util.FileWrapper(open(self.request_date.route().file_request, "rb"))



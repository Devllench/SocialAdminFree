# Класс WSGI приложения
from model.status_codes_class import StatusCodeClass
from model.response_headers_class import ResponseHeadersClass
import os, datetime, wsgiref
from wsgiref import util


class AppClass(object):
    # опрежедение класса
    def __init__(self, environ=None, start_response=None):
        # окружение приложения
        self.environ = environ
        # обьект для формирования запроса
        self.start = start_response
        self.status_codes = StatusCodeClass()
        self.response_headers = ResponseHeadersClass()

    # вызов обьекта класса во время запроса.
    def __iter__(self):
        # !
        url_request = self.get_url()
        print(str(datetime.datetime.now()) + '...1% get url:  :' + url_request)

        fn = self.get_file(url_request)
        print(str(datetime.datetime.now()) + '...2% get file:  :' + fn)

        # указываем status code и response_headers
        status_code = self.status_codes.status_ok
        response_headers = self.response_headers.create_response_headers(url_patch=url_request)
        self.start(status_code, response_headers)

        yield from self.return_string_page_in_body_answer(fn, url_request)
        print(str(datetime.datetime.now()) + '...100% answer: ' + status_code + ' | ' + str(response_headers) + ' | ' + url_request)

    def return_string_page_in_body_answer(self, fn, url_request):
        # Определяемм тело запроса исходя из цели запроса исходя из цели запроса
        # !
        # запрошен index http://localhost:8000/
        if url_request == "":
            # формируем строку тела запроса
            # закодировав  ее utf-8 в байты
            page = '<h1>Index<h1>'.encode()
            # возвращаем строку тела запроса
            yield page

        # запрошен home  http://localhost:8000/home
        elif url_request == 'home':
            # открываем файл нужный файл для формирования массива из строк файла
            with open(fn) as file:
                # формируем массив из строк
                array = [row.strip() for row in file]
            # вывводим построчно файл в тело запроса
            for j in array:
                # возвращаем строку тела запроса
                # закодировав  ее utf-8 в байты
                yield j.encode()

        # запрошен open.js  http://localhost:8000/open.js
        elif url_request == 'open.js':
            # указываем названия файла сходя из цели запроса
            fn = 'open.js'
            # открываем файл нужный файл для формирования массива из строк файла
            with open(fn) as file:
                # формируем массив из строк
                array = [row.strip() for row in file]
            # вывводим построчно файл в тело запроса
            for j in array:
                # возвращаем строку тела запроса
                # закодировав  ее utf-8 в байты
                yield j.encode()
        # запрошен open.js  http://localhost:8000/open.css
        elif url_request == 'open.css':
            # указываем названия файла сходя из цели запроса
            fn = 'open.css'
            # открываем файл нужный файл
            with open(fn) as file:
                # формируем массив из строк
                array = [row.strip() for row in file]
            # вывводим построчно файл в тело запроса
            for j in array:
                # возвращаем строку тела запроса
                # закодировав  ее utf-8 в байты
                yield j.encode()
        # !

    # метод для получения цели запроса path_info из URL запроса клиента
    def get_url(self):
        # получаем значение после URL
        urls = util.shift_path_info(self.environ)
        return urls

    # метод для определения необходимого файла исходя из цели запроса
    def get_file(self, path=None):
        # получаем цель запроса
        fn = os.path.join(path, self.environ['PATH_INFO'][1:])
        # если не точка цель запроса, то
        if '.' not in fn.split(os.path.sep)[-1]:
            # указываем файл для цели home
            fn = os.path.join('home.html')
        return fn

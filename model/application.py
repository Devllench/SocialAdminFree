# Класс WSGI приложения
from model.status_codes_class import StatusCodeClass
import os
import wsgiref
from wsgiref.util import FileWrapper
from wsgiref import headers, util
from io import StringIO
import mimetypes

import wsgiref


class AppClass(object):
    # опрежедение класса
    def __init__(self, environ=None, start_response=None):
        # окружение приложения
        self.environ = environ
        # обьект для формирования запроса
        self.start = start_response

    # вызов обьекта класса
    def __iter__(self):
        # указываем статус ответа
        status_codes = StatusCodeClass()

        # получаем  URL из запроса клиента соответствующий цели запроса внутри приложения.
        # (псоле http:exmp:8000/...)
        url = self.get_url()
        print('this url arthe /: ' + url)
        # выбираем нужный файл  для передачи клиену
        # исходя из остатока пути в URL соответствующий цели запроса внутри приложения
        fn = self.get_file(url)
        print('This is client file: ' + fn)
        # выбираем тип файла в Content-Type для корректного отображения в браузере
        # получаем цель запроса URL из запроса
        typ = os.path.join(url, self.environ['PATH_INFO'][1:])
        # Получаем имя файла для определения типа контента
        typ1 = self.get_file(url)
        print('1 met Content-type: ' + typ)
        print('2 met Content-type: ' + str(typ1))
        # переменная типа контаента для указания в response_headers
        typ_in = None
        # определяем тип конмтента для Content Type в в response_headers
        # по цели запроса
        # Здесь необходимо описать все возможные  типы запросов выполняющиеся к приложению браузером
        # цель запроса home
        if typ == 'home/':
            # выбираем для html файла
            typ_in = 'text/html'
        # цель запроса js файл используемый в home.html
        elif typ == 'open.js/':
            # выбираем для js файла
            typ_in = 'application/javascript'
        # цель запроса ccs файл используемый в в home.html
        elif typ == 'open.css/':
            # выбираем для css файла
            typ_in = 'text/css'
        # цель запроса index, корень сайта
        elif typ == '':
            typ_in = 'text/plain'

        print(' this is content-type: ' + typ_in)
        # вормируем заголовки для ответа клиенту

        # Указываем Content-Type
        response_headers = [('Content-type', typ_in + ';charset=utf-8')]
        # указываем статут и заголовки
        self.start(status_codes.status_ok, response_headers)

        # Определяемм тело запроса исходя из цели запроса

        # запрошен index http://localhost:8000/
        if url == "":
            # формируем строку тела запроса
            # закодировав  ее utf-8 в байты
            page = '<h1>Index<h1>'.encode()
            # возвращаем строку тела запроса
            yield page

        # запрошен home  http://localhost:8000/home
        elif url == 'home':
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
        elif url == 'open.js':
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
        elif url == 'open.css':
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

    # метод для получения цели запроса path_info из URL запроса клиента
    def get_url(self):
        # получаем значение после URL
        urls = util.shift_path_info(self.environ)
        return urls

    # метод для определения необходимого файла исходя из цели запроса
    def get_file(self, path=None):
        # получаем цель запроса
        fn = os.path.join(path, self.environ['PATH_INFO'][1:])
        print(fn)
        # если не точка цель запроса, то
        if '.' not in fn.split(os.path.sep)[-1]:
            # указываем файл для цели home
            fn = os.path.join('home.html')
            print(fn)
        return fn

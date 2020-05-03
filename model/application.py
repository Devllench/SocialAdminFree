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
        #self.response_headers = ResponseHeadersClass(url_path=util.shift_path_info(self.environ))

    # вызов обьекта класса во время запроса.
    def __iter__(self):
        # указываем status code и response_headers по умолчанию
        # !
        status_code = self.status_codes.status_ok
        #response_headers = [('Content-type, text/plain;charset=utf-8')]

        #response_headers = self.response_headers.create_response_headers()
        # !

        # Формируем response_headers
        # !
        # 1
        # получаем  URL из запроса клиента соответствующий цели запроса внутри приложения.
        # (псоле http:exmp:8000/...)
        url_request = self.get_url()
        # 1
        # 2
        # выбираем нужный файл  для передачи клиену
        # исходя из остатока пути в URL соответствующий цели запроса внутри приложения
        # Указываем Content-Type
        # 2
        fn = self.get_file(url_request)
        # Логируем событие.
        print(str(datetime.datetime.now()) + '...2% get file:  :' + fn)
        # 2
        # 3
        # Указываем Content-Type
        # формируем тип ответа клиенту
        typ_in = self.get_type_answer(url_request)
        # Логируем событие.
        print(str(datetime.datetime.now()) + '...3% get  Content-Type  :' + typ_in)
        # 2

        # указываем статут и заголовки исходя из запроса
        response_headers = [('Content-type', typ_in + ';charset=utf-8')]
        # !
        print(str(datetime.datetime.now()) + '...4% greate answer: ' + status_code + " | " + str(response_headers))
        self.start(str(status_code), response_headers)
        # !
        # возвращаем тело ответа на запрос клиента
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

    def get_type_answer(self, url_request):
        # выбираем тип файла в Content-Type для корректного отображения в браузере
        # получаем цель запроса URL из запроса
        typ = os.path.join(url_request, self.environ['PATH_INFO'][1:])
        # Получаем имя файла для определения типа контента
        # typ1 = self.get_file(url_request)
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
        return typ_in

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

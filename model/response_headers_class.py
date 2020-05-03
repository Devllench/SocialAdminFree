# Класс Status Codes
class ResponseHeadersClass(object):
    def __init__(self, url_path, headers_default=None):
        if headers_default is None:
            headers_default = [('Content-type', 'text/html;charset=utf-8')]
        self.headers_default = headers_default
        self.url_patch = url_path

    def create_response_headers(self):
        typ_in = None
        if self.url_patch == '':
            # выбираем для js файла
            typ_in = 'text/html'
            self.headers_default = [('Content-type', typ_in + ';charset=utf-8')]
            return self.headers_default

        elif self.url_patch == 'home':
            # выбираем для html файла
            typ_in = 'text/html'
            self.headers_default = [('Content-type', typ_in + ';charset=utf-8')]
            return self.headers_default

        # цель запроса js файл используемый в home.html
        elif self.url_patch == 'open.js':
            # выбираем для js файла
            typ_in = 'application/javascript'
            self.headers_default = [('Content-type', typ_in + ';charset=utf-8')]
            return self.headers_default

        # цель запроса ccs файл используемый в в home.html
        elif self.url_patch == 'open.css':
            # выбираем для css файла
            typ_in = 'text/css'
            # цель запроса index, корень сайта
            self.headers_default = [('Content-type', typ_in + ';charset=utf-8')]
            return self.headers_default

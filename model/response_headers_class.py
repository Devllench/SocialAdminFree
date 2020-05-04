# Класс создания заголовков ответа
class ResponseHeadersClass(object):
    def __init__(self, headers_default=None):
        self.headers_default = str(headers_default)

    def create_response_headers(self, type_in):
        self.headers_default = [('Content-type', type_in + ';charset=utf-8')]
        return self.headers_default



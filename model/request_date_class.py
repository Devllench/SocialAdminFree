# Класс запрос клиента
# данный класс должен определять является ли запрос валидным и затем указываеться соотвествубщие данные
from model.request_pattern_class import RequestPatternClass
from model.status_codes_class import StatusCodeClass
from model.response_headers_class import ResponseHeadersClass


class RequestClintClass(object):
    def __init__(self, url_path_info=None, answer_page=None):
        self.url_path_info = url_path_info
        self.status_response_code = StatusCodeClass()
        self.response_headers = ResponseHeadersClass()
        self.answer_page = answer_page

    def route(self):
        page_home = RequestPatternClass(url_request='home',
                                        file_request='home.html',
                                        content_type='text/html',
                                        status_code=self.status_response_code.status_ok)

        page_index = RequestPatternClass(url_request='',
                                         file_request='index.html',
                                         content_type='text/html',
                                         status_code=self.status_response_code.status_ok)

        page_not_found = RequestPatternClass(url_request=None,
                                             file_request='404.html',
                                             content_type='text/html',
                                             status_code=self.status_response_code.status_not_found)

        page_js = RequestPatternClass(url_request='open.js',
                                      file_request='open.js',
                                      content_type='application/javascript',
                                      status_code=self.status_response_code.status_ok)

        page_css = RequestPatternClass(url_request='open.css',
                                       file_request='open.css',
                                       content_type='text/css',
                                       status_code=self.status_response_code.status_ok)

        if self.url_path_info == page_index.url_request:
            self.answer_page = page_index

        elif self.url_path_info == page_home.url_request:
            self.answer_page = page_home

        elif self.url_path_info == page_js.url_request:
            self.answer_page = page_js

        elif self.url_path_info == page_css.url_request:
            self.answer_page = page_css
        else:
            self.answer_page = page_not_found

        return self.answer_page

    def get_headers(self):
        return self.response_headers.create_response_headers(self.route().content_type)

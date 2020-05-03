# Класс запрос клиента
# данный класс должен определять является ли запрос валидным и затем указываеться соотвествубщие данные


class RequestClintClass(object):
    def __init__(self, url_path_info=None):
        self.url_path_info = url_path_info
        self.file_req = '404.html'

    def route(self):
        url_pattern = ['', 'home', 'testcl']
        file_req_pattern = ['open.js', 'open.css']
        file_path = ['home.html', 'open.js', 'open.css', '404.html', '500.html']

        if self.url_path_info == url_pattern[0]:
            self.file_req = 'index.html'
            return self.file_req

        elif self.url_path_info == url_pattern[1]:
            self.file_req = 'home.html'
            return self.file_req

        elif self.url_path_info == url_pattern[2]:
            self.file_req = 'index.html'
            return self.file_req

        elif self.url_path_info in file_req_pattern:
            return self.url_path_info

        else:
            return self.file_req



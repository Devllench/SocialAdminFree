# класс образцов запроса
class RequestPatternClass(object):
    def __init__(self, url_request=None, file_request=None, content_type=None, status_code=None):
        self.url_request = url_request
        self.file_request = file_request
        self.content_type = content_type
        self.status_code = status_code


# Класс Status Codes
class StatusCodeClass(object):
    def __init__(self, status_ok='200 OK', status_err='500 Error', status_not_found='404 Not Found'):
        self.status_ok = status_ok
        self.status_err = status_err
        self.status_not_found = status_not_found

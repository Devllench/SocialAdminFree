# Класс тела ответа
class ResponseBodyClass(object):
    def __init__(self, string_body_hello=b'Hello page', string_body_err=b'ERROR!', string_body_no_found=b'NOT FOUND' ):
        self.string_body_hello = string_body_hello
        self.string_body_err = string_body_err
        self.string_body_no_found = string_body_no_found

    def create_string_body(self, file_patch):
        with open(file_patch) as file:
            # формируем массив из строк
            array = [row.strip() for row in file]
        # вывводим построчно файл в тело запроса
        for j in array:
            # возвращаем строку тела запроса
            # закодировав  ее utf-8 в байты
            yield j.encode()


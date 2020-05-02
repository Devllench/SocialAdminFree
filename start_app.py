from wsgiref.simple_server import make_server
from model.application import AppClass
import sys




#запуск сервера wsgi
if __name__ == '__main__':
    # указываем покт
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
    # создаем обьект приложения из его класса
    app = AppClass
    # созаем http сервер
    httpd = make_server('', port, app)
    print("Serving  on port , control-C to stop".format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down.")
        httpd.server_close()

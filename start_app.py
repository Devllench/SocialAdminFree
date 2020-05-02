from wsgiref.simple_server import make_server
from model.application import AppClass
import sys




#запуск сервера wsgi
if __name__ == '__main__':
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
    hello_world_app = AppClass
    httpd = make_server('', port, hello_world_app)
    print("Serving  on port , control-C to stop".format(port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down.")
        httpd.server_close()

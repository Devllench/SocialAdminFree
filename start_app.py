from wsgiref.simple_server import make_server
from model.application import AppClass
import sys
import os
import mimetypes
from wsgiref import simple_server, util

hello_world_app = AppClass

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
    httpd = make_server('', port, hello_world_app)
    print("Serving {} on port {}, control-C to stop".format(path, port))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down.")
        httpd.server_close()

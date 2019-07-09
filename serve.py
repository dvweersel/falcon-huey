from waitress import serve
from falcon.api import test

if __name__ == '__main__':
    serve(test, host='0.0.0.0', port=5555)

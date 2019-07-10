from waitress import serve
from falcon_api import create_api

if __name__ == '__main__':
    api = create_api()
    serve(api, host='0.0.0.0', port=5555)

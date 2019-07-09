from waitress import serve
from falcon_api.serve import api

if __name__ == '__main__':
    serve(api, host='0.0.0.0', port=5555)

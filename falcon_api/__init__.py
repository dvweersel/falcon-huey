import falcon
from falcon_cors import CORS
from falcon_api.routes import register_routes

def create_api():

    cors = CORS(allow_all_origins=True)
    api = falcon.API(middleware=[cors.middleware])

    register_routes(api)

    return api

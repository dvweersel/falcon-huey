import falcon
from falcon_cors import CORS
from falcon_api.routes import register_routes
from huey import RedisHuey

# Need to figure out how to make this work with the application factory pattern
# huey = RedisHuey('queue', immediate=True)
huey_queue = RedisHuey('queue', immediate=True)


def create_api():
    cors = CORS(allow_all_origins=True)
    api = falcon.API(middleware=[cors.middleware])

    register_routes(api)

    return api

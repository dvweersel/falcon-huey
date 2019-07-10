import falcon
from falcon_cors import CORS
from falcon_api.resources.APIStatus import APIStatus
from falcon_api.resources.Model import Fit, Predict


def create_api():

    cors = CORS(allow_all_origins=True)
    api = falcon.API(middleware=[cors.middleware])

    register_routes(api)

    return api


def register_routes(api):
    # api.add_route('/model/predict', Predict())
    # api.add_route('/model/fit/{algo}', Fit())
    api.add_route('/', APIStatus())

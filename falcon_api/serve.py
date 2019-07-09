import falcon
from falcon_api.resources import Predict

api = falcon.API()

api.add_route('/predict', Predict())

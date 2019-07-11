from falcon_api.resources.APIStatus import APIStatus
from falcon_api.resources.Model import Fit, Predict
from falcon_api.resources.Task import Task, TaskStatus


def register_routes(api):
    api.add_route('/', APIStatus())
    api.add_route('/model/predict', Predict())
    api.add_route('/model/fit', Fit())
    api.add_route('/task', Task())
    api.add_route('/task/{id}', TaskStatus())

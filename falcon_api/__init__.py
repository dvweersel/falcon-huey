import falcon
import json

api = falcon.API()


class APIStatus:

    @staticmethod
    def on_get(req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps('pong')


api.add_route('/ping', APIStatus())
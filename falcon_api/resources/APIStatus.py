import falcon
import json

class APIStatus:

    @staticmethod
    def on_get(req, resp):
        resp.status = falcon.HTTP_200
        resp.body = json.dumps('API is online')
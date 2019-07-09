import parser
import json


class Predict(object):
    @staticmethod
    def on_get(req, resp):
        """Handles GET requests"""
        data = parser.parse_args(req)

        resp.body = json.dumps('Pong')
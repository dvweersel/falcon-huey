import json
from falcon_api.data.dummy import get_data
from falcon_api.model.model import Regressor
import jsonpickle
import json


class Fit:
    @staticmethod
    def on_post(req, resp):
        x, y = get_data()

        query = json.loads(req.stream.read())  # this is how you capture POST content

        d = int(query['degree'])
        model = Regressor(d)
        model.fit(x, y)
        save(model)
        resp.body = json.dumps({'success': "Model artefact written in JSON format", 'components': model.B.tolist()})

    @staticmethod
    def on_get(req, resp, d):
        x, y = get_data()

        model = Regressor(d)
        model.fit(x, y)
        save(model)
        resp.body = json.dumps({'success': "Model artefact written in JSON format", 'components': model.B.tolist()})


class Predict:
    @staticmethod
    def on_get(req, resp):
        query = json.loads(req.stream.read())
        x = int(query['x'])

        try:
            model = load()
            resp.body = json.dumps(model.predict(x).tolist())  # predict on the same x (!)
        except FileNotFoundError:
            resp.body = json.dumps(
                {'error': "Model not trained yet"})

    @staticmethod
    def on_get(req, resp, x):
        try:
            model = load()
            resp.body = json.dumps(model.predict(x).tolist())  # predict on the same x (!)
        except FileNotFoundError:
            resp.body = json.dumps(
                {'error': "Model not trained yet"})


def save(model, path='data/model.json'):
    with open(path, 'w') as f:
        json.dump(jsonpickle.encode(model), f)  # making sure the output is serializable


def load(path='data/model.json'):
    with open(path, 'r') as f:
        m = f.read()
    return jsonpickle.decode(json.loads(m))


# class Score:
#
#     def on_get(self, req, resp):
#         try:
#             e = Evaluate(y)
#             m = load()
#             resp.body = json.dumps(e.score(m.predict(x)))  # deviation du to fuzz factor
#         except FileNotFoundError:
#             resp.body = json.dumps(
#                 {'error': "Model not trained yet; visit one of the '/fit/{multi,poly}' endpoints first"})

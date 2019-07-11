from falcon_api.data.dummy import get_data
from falcon_api.model.model import Regressor
import json


class Fit:
    @staticmethod
    def on_post(req, resp):
        """
            Fits a regressor with degree d
        """
        x, y = get_data()

        d = int(req.media.get('d'))

        model = Regressor(degree=d)
        score = model.fit(x, y)
        model.save()

        resp.body = json.dumps({'success': "Model artefact written in JSON format",
                                'components': model.get_components(),
                                'score': score})

    @staticmethod
    def on_get(req, resp):
        """
            Returns the fitted regressor
        """
        model = Regressor()
        model.load()

        params = model.get_params()
        print(f"Parameters of loaded model {params}")
        resp.body = json.dumps({'components' : model.get_components()})


class Predict:

    @staticmethod
    def on_post(req, resp):
        try:
            model = Regressor()
            x = req.media.get('x')
            if isinstance(x, list):
                model.load()
                resp.body = json.dumps(model.predict(x).tolist())  # predict on the same x (!)
            else:
                resp.body = json.dumps({'error': 'TypeError: Input should be a list'})
        except FileNotFoundError:
            resp.body = json.dumps({'error': "Model not trained yet"})

    @staticmethod
    def on_get(req, resp):
        try:
            model = Regressor()
            model.load()
            x = int(req.media.get('x'))

            resp.body = json.dumps(model.predict(x).tolist())  # predict on the same x (!)
        except FileNotFoundError:
            resp.body = json.dumps({'error': "Model not trained yet"})


class Score:

    def on_get(self, req, resp):
        try:
            e = Evaluate(y)
            m = load()
            resp.body = json.dumps(e.score(m.predict(x)))  # deviation du to fuzz factor
        except FileNotFoundError:
            resp.body = json.dumps(
                {'error': "Model not trained yet; visit one of the '/fit/{multi,poly}' endpoints first"})

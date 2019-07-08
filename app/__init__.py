from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from .views.main.main import main
from .extensions import db
from .config import *


def create_app(config=BaseConfig):
    app = Flask(__name__)

    app.config.from_object(config)
    register_blueprints(app)

    db.init_app(app)

    return app


def register_blueprints(app):
    app.register_blueprint(main)

from flask import Flask
from db import setup_db, setup_migration
from routes import *


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.url_map.strict_slashes = False
    setup_db(app)

    # register models
    from models import Actor, Movie
    app.register_blueprint(actors_router)
    app.register_blueprint(movies_router)

    return app

from flask import Flask
from routes.actors import bp as actorRoute
from app.db import setup_db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('config')
    app.url_map.strict_slashes = False
    app.register_blueprint(actorRoute)

    setup_db(app)

    @app.route('/hello')
    def hello():
        return app.config["HELLOWORLD"]
    return app

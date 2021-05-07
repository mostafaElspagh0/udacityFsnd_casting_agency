from flask import Flask
from routes.actors import bp as actorRoute


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('config')
    app.url_map.strict_slashes = False
    app.register_blueprint(actorRoute)

    @app.route('/hello')
    def hello():
        return app.config["HELLOWORLD"]
    return app

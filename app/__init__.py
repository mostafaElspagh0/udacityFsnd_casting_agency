from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('config')
    
    @app.route('/hello')
    def hello():
        return app.config["HELLOWORLD"]
    return app

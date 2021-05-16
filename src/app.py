from flask import Flask
from flask.json import jsonify
from src.database import setup_db
from src.routes import *

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.url_map.strict_slashes = False
    setup_db(app)

    # register models
    from src.database import Actor, Movie
    app.register_blueprint(actors_router)
    app.register_blueprint(movies_router)
    register_my_own_error_handler(app)
    
    @app.route('/', methods=['GET'])
    def healthy():
        return "healthy"

   
    return app

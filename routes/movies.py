from flask import jsonify, Blueprint
from flask.globals import request
from auth import requires_auth
from models.movie import Movie
from db import db
bp = Blueprint('movies', __name__, url_prefix='/movies')


@bp.route('/', methods=['GET'])
@requires_auth('get:movies')
def get_movies(payload):
    page = int(request.args.get('page', default='1', type=int))
    per_page = int(request.args.get('per_page', default='10', type=int))
    movies = Movie.query.paginate(
        page=page, per_page=per_page).items
    return jsonify({
        "success": True,
        "movies": [
            movie.toDict() for movie in movies
        ],
        'code': 200
    }), 200


@bp.route('/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(payload,id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({
        "success": True,
        "actors": [movie.toDict()],
        'code': 200,
    }), 200


@bp.route('/', methods=['POST'])
@requires_auth('add:movies')
def post_movies(payload):
    json_data = request.json
    title = json_data['title']
    release_date = json_data['release_date']
    new_movie = Movie(title=title, release_date=release_date)
    try:
        db.session.add(new_movie)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return jsonify({
            "success": False,
            "error": Exception.__repr__(),
            'code': 500,
        }), 500
    finally:
        db.session.close()

    return jsonify({
        "success": True,
        "movies": [new_movie.toDict()]
    }), 201


@bp.route('/<int:id>', methods=['PATCH'])
@requires_auth('patch:actors')
def patch_actors(payload, id):
    json_data = request.json
    actor = Actor.query.get(id)
    actor.update(json_data)
    return jsonify({
        "success": True,
        "actors": [actor.toDict()]
    }), 200


from flask import jsonify, Blueprint
from flask.globals import request
from src.auth import requires_auth
from src.db import Movie
from src.db import db
import datetime
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
        'code': "SUCCESS"
    }), 200


@bp.route('/<int:id>', methods=['GET'])
@requires_auth('get:movies')
def get_movies_by_id(payload, id):
    movie: Movie = Movie.query.get(int(id))
    if movie is None:
        return jsonify({
            "success": False,
            'code': "NOT FOUND",
        }), 404
    else:
        return jsonify({
            "success": True,
            "movies": [movie.toDict()],
            'code': "SUCCESS",
        }), 200


@bp.route('/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(payload, id):
    movie: Movie = Movie.query.get(int(id))
    if movie is None:
        return jsonify({
            "success": False,
            'code': "NOT FOUND",
        }), 404

    error = None

    try:
        movie_dict = movie.toDict()
        db.session.delete(movie)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        error = e
    finally:
        db.session.close()

    if error is None:
        return jsonify({
            "success": True,
            "movies": [movie_dict],
            'code': "DELETED",
        }), 202
    else:
        return jsonify({
            "success": False,
            'code': "INTERNAL SERVER ERROR",
            "error": str(error),
        }), 500


@bp.route('/', methods=['POST'])
@requires_auth('add:movies')
def post_movies(payload):
    json_data = request.json
    title = json_data['title']
    release_date = json_data['release_date']
    release_date = datetime.datetime.strptime(
        release_date, '%Y-%m-%d %H:%M:%S.%f')
    new_movie = Movie(title=title, release_date=release_date)
    error = None
    try:
        db.session.add(new_movie)
        db.session.commit()
        movie_dict = new_movie.toDict()
    except Exception as e:
        error = e
        db.session.rollback()

    finally:
        db.session.close()

    if error is None:
        return jsonify({
            "success": True,
            "movies": [movie_dict],
            "code": "CREATED"
        }), 201

    else:
        return jsonify({
            "success": False,
            "error": str(error),
            'code': "INTERNAL SERVER ERROR",
        }), 500


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

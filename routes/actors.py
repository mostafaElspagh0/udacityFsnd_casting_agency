from flask import jsonify, Blueprint
from auth import requires_auth
from models.actor import Actor
from app.db import db

bp = Blueprint('actors', __name__, url_prefix='/actors')


@bp.route('/', methods=['GET'])
@requires_auth('get:actors')
def get_actors():
    page = request.args.get('page', default='1', type=int)
    per_page = request.args.get('per_page', default='10', type=int)
    actors = Actor.query.paginate(
        page=page, per_page=per_page)
    return jsonify({
        "success": True,
        "actors": [
            actor.toDict() for actor in actors
        ],
        'code': 200
    }), 200


@bp.route('/<id:int>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors(id):
    actor = Actor.query.get(id)
    db.session.delete(actor)
    db.session.commit()
    return jsonify({
        "success": True,
        "actors": [actor.toDict()]
        'code': 204,
    }), 200


@bp.route('/', methods=['POST'])
@requires_auth('add:actors')
def post_actors():
    json_data = request.json
    name = json_data['name']
    age = json_data['age']
    gender = json_data['gender']
    new_actor = Actor(name=name, age=age, gender=gender)
    session = db.session
    try:
        db.session.add(new_actor)
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
        "actors": [new_actor.toDict()]
    }), 201


@bp.route('/<id:int>', methods=['PATCH'])
@requires_auth('patch:actors')
def get_actors(id):
    json_data = request.json
    actor = Actor.query.get(id)
    actor.update(json_data)
    return jsonify({
        "success": True,
        "actors": [actor.toDict()]
    }), 200

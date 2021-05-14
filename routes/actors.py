from os import error
from flask import jsonify, Blueprint, request
from sqlalchemy.orm.session import Session
from auth import requires_auth
from models.actor import Actor
from db import db

bp = Blueprint('actors', __name__, url_prefix='/actors')


@bp.route('/', methods=['GET'])
@requires_auth('get:actors')
def get_actors(payload):
    page = int(request.args.get('page', default='1', type=int))
    per_page = int(request.args.get('per_page', default='10', type=int))
    actors = Actor.query.paginate(
        page=page, per_page=per_page).items
    return jsonify({
        "success": True,
        "actors": [
            actor.toDict() for actor in actors
        ],
        'code': 200
    }), 200


@bp.route('/<int:id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors(payload, id):
    actor = Actor.query.get(id)
    db.session.delete(actor)
    db.session.commit()
    return jsonify({
        "success": True,
        "actors": [actor.toDict()],
        'code': 204,
    }), 200


@bp.route('/', methods=['POST'])
@requires_auth('add:actors')
def post_actors(payload):
    json_data = request.json
    name = json_data['name']
    age = json_data['age']
    gender = json_data['gender']
    new_actor = Actor(name=name, age=age, gender=gender)
    error = False
    try:
        db.session.add(new_actor)
        db.session.commit()
        actor_dict = new_actor.toDict()
    except Exception as k:
        e = k
        db.session.rollback()
        error = True
    finally:
        db.session.close()

    if not error:
        return jsonify({
            "success": True,
            "actors": [actor_dict]
        }), 201
    else:
        return jsonify({
            "success": False,
            "ex": str(e),
            'code': 500,
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

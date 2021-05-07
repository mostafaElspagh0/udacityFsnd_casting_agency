from flask import jsonify, Blueprint
from auth import requires_auth
from models.actor import Actor
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


@bp.route('/', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actors():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200


@bp.route('/', methods=['POST'])
@requires_auth('add:actors')
def post_actors():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200


@bp.route('/', methods=['PATCH'])
@requires_auth('patch:actors')
def get_actors():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200

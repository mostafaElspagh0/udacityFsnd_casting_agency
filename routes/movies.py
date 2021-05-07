from flask import jsonify, Blueprint
from auth import requires_auth
bp = Blueprint('movies', __name__, url_prefix='/movies')


@bp.route('/', methods=['GET'])
@requires_auth('get:movies')
def get_movies():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200


@bp.route('/', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200


@bp.route('/', methods=['POST'])
@requires_auth('add:movies')
def post_movies():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200


@bp.route('/', methods=['PATCH'])
@requires_auth('patch:movies')
def patch_movies():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200

from flask import jsonify,Blueprint

bp = Blueprint('actors', __name__, url_prefix='/actors')

@bp.route('/', methods=['GET'])
def get_actors():
    # TODO//: implemet endpoint
    return jsonify({
        "success": False,
        "error": "not implemented"
    }), 200

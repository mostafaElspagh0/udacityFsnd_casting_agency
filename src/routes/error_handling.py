from flask import Flask
from flask import json
from flask.json import jsonify

from auth import AuthError


def register_my_own_error_handler(app: Flask):
    @app.errorhandler(AuthError)
    def handle_auth_error(e: AuthError):
        return jsonify({
            "success": False,
            "error": e.error,
            'code': "AuthError",
        }), 401

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({
            "success": False,
            "error": str(error),
            'code': "NotFound",
        }), 404

    @app.errorhandler(404)
    def handle_internel_server_error(error):
        return jsonify({
            "success": False,
            'code': "INTERNAL SERVER ERROR",
            "error": str(error),
        }), 500

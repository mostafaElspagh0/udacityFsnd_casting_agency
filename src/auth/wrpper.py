from functools import wraps
from src.auth.AuthError import AuthError
from jose import jwt
from config import *
from src.auth.utils import (get_token_auth_header,
                            verify_decode_jwt, check_permissions)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            allow_expired_tokens = os.getenv("ALLOW_EXPIRED_TOKENS")
            if allow_expired_tokens == "1":
                payload = jwt.get_unverified_claims(token)
            else:
                payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)

        return wrapper

    return requires_auth_decorator

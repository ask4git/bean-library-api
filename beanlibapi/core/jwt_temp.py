import jwt
import time

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpRequest

from jwt.exceptions import ExpiredSignatureError, DecodeError, InvalidTokenError


def generate_jwt_token_payload(user) -> dict:
    current_time = time.time()
    expiration_timestamp = current_time + settings.JWT_ACCESS_TOKEN_LIFETIME

    return {
        "id": int(user.id),
        "expire": int(expiration_timestamp)
    }


def generated_jwt_token(payload) -> str:
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


def authenticate_jwt(request: HttpRequest):
    auth_header = request.META.get('HTTP_AUTHORIZATION', None)

    if auth_header is None:
        return None

    try:
        token = auth_header.split()[-1]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_model = get_user_model()
        user = user_model.objects.get(id=payload['id'])
        return user
    except (ExpiredSignatureError, DecodeError, InvalidTokenError):
        return None

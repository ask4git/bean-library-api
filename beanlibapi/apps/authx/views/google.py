import requests
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from allauth.core.internal.httpkit import redirect
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView, SocialConnectView

from django.core.exceptions import ValidationError
import logging

logger = logging.getLogger(__name__)


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    # callback_url = settings.GOOGLE_LOGIN_URL
    client_class = OAuth2Client


class GoogleConnectView(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter


@api_view(['GET'])
def google_login_api_view(request):
    response = redirect(
        f"{settings.GOOGLE_OAUTH2_API}?"
        f"client_id={settings.GOOGLE_OAUTH2_CLIENT_ID}&"
        f"response_type=code&"
        f"redirect_uri={settings.BASE_BACKEND_URL}/auth/signup/google/callback&"
        f"scope={settings.GOOGLE_SCOPE_USERINFO}&"
        f"prompt=select_account"
    )
    return response


@api_view(['GET'])
def google_callback_api_view(request):
    code = request.GET.get('code')
    google_token_api = settings.GOOGLE_OAUTH2_TOKEN_API

    access_token = google_get_access_token(google_token_api, code)

    userinfo = google_get_userinfo(access_token=access_token)

    profile_data = {
        'username': userinfo['email'],
        'first_name': userinfo.get('given_name', ''),
        'last_name': userinfo.get('family_name', ''),
        'nickname': userinfo.get('nickname', ''),
        'name': userinfo.get('name', ''),
        'image': userinfo.get('picture', None),
        'path': "google",
        'access_token': access_token,
    }

    print(userinfo)
    print(profile_data)

    return Response(profile_data)


def google_get_access_token(google_token_api, code):
    token_response = requests.post(
        google_token_api,
        params={
            'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
            'client_secret': settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': f'{settings.BASE_BACKEND_URL}/auth/signup/google/callback',
            'state': 'random_string'
        }
    )

    if not token_response.ok:
        raise ValidationError('google_token is invalid')

    access_token = token_response.json().get('access_token')
    return access_token


def google_get_userinfo(access_token):
    userinfo_response = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        params={
            'access_token': access_token
        }
    )

    if not userinfo_response.ok:
        raise ValidationError('Failed to obtain user info from Google.')

    user_info = userinfo_response.json()
    return user_info

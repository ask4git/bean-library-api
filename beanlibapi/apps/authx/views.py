from allauth.core.internal.httpkit import redirect
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView, SocialConnectView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions as p
from rest_framework.response import Response
import requests
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class GoogleConnectView(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter


def google_get_access_token(google_token_api, code):
    client_id = settings.GOOGLE_OAUTH2_CLIENT_ID
    client_secret = settings.GOOGLE_OAUTH2_CLIENT_SECRET
    code = code
    grant_type = 'authorization_code'
    # redirection_uri = settings.BASE_BACKEND_URL + "/api/v1/auth/login/google/callback"
    redirect_uri = settings.BASE_BACKEND_URL + "/auth/signup/google/callback"
    state = "random_string"

    # google_token_api += \
    #     f"?client_id={client_id}&client_secret={client_secret}&code={code}&grant_type={grant_type}&redirect_uri={redirection_uri}&state={state}"
    #
    # token_response = requests.post(google_token_api)
    token_response = requests.post(
        google_token_api,
        params={
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code,
            'grant_type': grant_type,
            'redirect_uri': redirect_uri,
            'state': state,
        }
    )

    print(token_response.status_code)
    print(token_response.json())

    if not token_response.ok:
        raise ValidationError('google_token is invalid')

    access_token = token_response.json().get('access_token')

    return access_token


def google_get_user_info(access_token):
    user_info_response = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        params={
            'access_token': access_token
        }
    )

    if not user_info_response.ok:
        raise ValidationError('Failed to obtain user info from Google.')

    user_info = user_info_response.json()

    return user_info


# http://localhost:8000/auth/signup/google/
class GoogleLoginApiView(APIView):
    # permission_classes = [p.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        app_key = settings.GOOGLE_OAUTH2_CLIENT_ID
        scope = "https://www.googleapis.com/auth/userinfo.email " + \
                "https://www.googleapis.com/auth/userinfo.profile"

        redirect_uri = f"{settings.BASE_BACKEND_URL}/auth/signup/google/callback"

        response = redirect(
            f"{settings.GOOGLE_OAUTH2_API}/auth?"
            f"client_id={app_key}&"
            f"response_type=code&"
            f"redirect_uri={redirect_uri}&"
            f"scope={scope}"
        )

        return response


class GoogleCallbackApiView(APIView):
    permission_classes = [p.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        google_token_api = "https://oauth2.googleapis.com/token"

        access_token = google_get_access_token(google_token_api, code)
        print(access_token)
        user_data = google_get_user_info(access_token=access_token)
        print(user_data)

        profile_data = {
            'username': user_data['email'],
            'first_name': user_data.get('given_name', ''),
            'last_name': user_data.get('family_name', ''),
            'nickname': user_data.get('nickname', ''),
            'name': user_data.get('name', ''),
            'image': user_data.get('picture', None),
            'path': "google",
            'access_token': access_token,
        }

        print("?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!?!")
        user_info_response = requests.get(
            # "https://www.googleapis.com/oauth2/v3/userinfo",
            f"{settings.GOOGLE_OAUTH2_API}/userinfo",
            params={
                'access_token': access_token
            }
        )
        print(user_info_response)

        print(profile_data)
        return Response(profile_data)


@api_view(['POST'])
def send_email(request, ):
    if request.method == "POST":
        send_mail(
            'Title',
            'Contentsss',
            from_email=settings.GMAIL_DEFAULT_SENDER,
            recipient_list=['ask4git@gmail.com'],
        )
    return render(request, 'email.html')

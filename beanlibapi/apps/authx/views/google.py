from django.conf import settings
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView, SocialConnectView


class GoogleLoginView(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.GOOGLE_OAUTH2_REDIRECT_URL
    client_class = OAuth2Client


class GoogleConnectView(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter

# # Temporary Deprecated
# def google_get_access_token(code):
#     token_response = requests.post(
#         "https://oauth2.googleapis.com/token",
#         params={
#             'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
#             'client_secret': settings.GOOGLE_OAUTH2_CLIENT_SECRET,
#             'code': code,
#             'grant_type': 'authorization_code',
#             'redirect_uri': settings.GOOGLE_OAUTH2_REDIRECT_URL,
#             'state': 'random_string'
#         }
#     )
#
#     if not token_response.ok:
#         raise ValidationError('google_token is invalid')
#
#     access_token = token_response.json().get('access_token')
#     return access_token
#
# # Temporary Deprecated
# def google_get_userinfo(access_token):
#     userinfo_response = requests.get(
#         "https://www.googleapis.com/oauth2/v3/userinfo",
#         params={
#             'access_token': access_token
#         }
#     )
#
#     if not userinfo_response.ok:
#         raise ValidationError('Failed to obtain user info from Google.')
#
#     user_info = userinfo_response.json()
#     return user_info

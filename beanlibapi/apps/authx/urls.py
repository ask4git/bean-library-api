from django.conf import settings
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from dj_rest_auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)

from dj_rest_auth.registration.views import (
    RegisterView,
)
from beanlibapi.apps.authx.views import (
    GoogleLoginApiView,
    GoogleCallbackApiView,
    GoogleLoginView,
    GoogleConnectView,
    send_email,
)
from rest_framework_simplejwt.views import TokenVerifyView

from dj_rest_auth.jwt_auth import get_refresh_view
app_name = 'authx'

urlpatterns = []

urlpatterns += [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('password/change/', PasswordChangeView.as_view(), name='password_change'),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    # path('token/verify/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('email/send/', send_email, name='send_email'),
]

urlpatterns += [
    path("signup/google/", GoogleLoginApiView.as_view(), name="signup_google"),
    path("signup/google/callback", GoogleCallbackApiView.as_view(), name="signup_google_callback"),
    path('api/social-login/google/', GoogleLoginView.as_view(), name='google_login'),
    path('api/social-login/connect/google/', GoogleConnectView.as_view(), name='google_login'),
]

urlpatterns += [
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
]




urlpatterns = format_suffix_patterns(urlpatterns)

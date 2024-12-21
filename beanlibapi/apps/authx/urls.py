from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from dj_rest_auth.views import (
    LoginView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from dj_rest_auth.registration.views import (
    ResendEmailVerificationView,
)
from beanlibapi.apps.authx.views.base import (
    RegisterView,
    send_email,
    CustomEmailVerification,
)
from beanlibapi.apps.authx.views.google import (
    GoogleLoginView,
    GoogleConnectView,
)
from allauth.account.views import email as allauth_email_view

app_name = 'authx'

urlpatterns = []

urlpatterns += [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('email/', allauth_email_view, name='account_email'),
    # path('resend-confirm-email/', CustomEmailVerification.as_view(), name='resend_confirm_email'),
    path('resend-confirm-email/', ResendEmailVerificationView.as_view(), name="rest_resend_email"),
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
    path('api/social-login/google/', GoogleLoginView.as_view(), name='google_login'),
    path('api/social-login/connect/google/', GoogleConnectView.as_view(), name='google_loginconnect'),
]

urlpatterns += [
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

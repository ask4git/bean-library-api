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
from beanlibapi.apps.authx import views_temp

app_name = 'authx'

urlpatterns = []

urlpatterns += [
    # path('', include('dj_rest_auth.urls')),
    path('sign-up/', RegisterView.as_view(), name='sign-up'),

    path('sign-in/', LoginView.as_view(), name='sign-in'),

    path('password/change/', PasswordChangeView.as_view(), name='password_change'),

    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),

    path('password/reset/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views_temp.login_view, name='login_temp'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

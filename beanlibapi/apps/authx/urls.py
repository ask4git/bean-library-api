from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from beanlibapi.apps.authx import views
from beanlibapi.apps.authx import views_temp

app_name = 'authx'

urlpatterns = []

urlpatterns += [
    # path('', include('dj_rest_auth.urls')),
    path('sign-up/', views.RegisterView.as_view(), name='custom_register'),
    path('sign-in/', views.LoginView.as_view(), name='custom_login'),
    # path('auth/sign-out/', views.UserRegisterView.as_view(), name='custom_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views_temp.login_view, name='login_temp'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

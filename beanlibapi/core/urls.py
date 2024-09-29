from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from beanlibapi.core import views as v
from beanlibapi.core import views_temp

app_name = 'core'

urlpatterns = []

# auth
urlpatterns += [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/sign-up/', v.RegisterView.as_view(), name='custom_register'),
    path('auth/sign-in/', v.LoginView.as_view(), name='custom_login'),
    # path('auth/sign-out/', v.UserRegisterView.as_view(), name='custom_register'),

    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns += [
    path('bean/', v.BeanListCreateView.as_view()),
    path('bean/<str:pk>/', v.BeanRetrieveUpdateDestroyView.as_view()),
]

# temp
urlpatterns += [
    path('users/login/', views_temp.login_view, name='login_temp'),
    path('books/', views_temp.protected_view, name='books_temp'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

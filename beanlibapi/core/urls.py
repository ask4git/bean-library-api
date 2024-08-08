from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from beanlibapi.core import views
from beanlibapi import core
from beanlibapi.core.views import LoginView

app_name = 'core'
urlpatterns = [
    path('loginn/', LoginView.as_view(), name='login'),
]

urlpatterns += [
    path('bean/', views.BeanListCreateView.as_view()),
    path('bean/<str:pk>/', views.BeanRetrieveUpdateDestroyView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

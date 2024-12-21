from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView

from dj_rest_auth.registration.views import RegisterView as _RegisterView
from allauth.account.adapter import get_adapter

from beanlibapi.apps.authx.serializers import RegisterSerializer


class RegisterView(_RegisterView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = super().perform_create(serializer)
        # Todo: logging
        return user


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


class CustomEmailVerification(APIView):
    def get(self, request):
        pass

    def post(self, request):
        adapter = get_adapter()
        adapter.is_email_verified()

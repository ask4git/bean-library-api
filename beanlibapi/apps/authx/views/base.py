from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions as p

from django.core.mail.message import EmailMessage
from django.conf import settings

from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from django.core.mail import send_mail
from django.conf import settings

from allauth.account.adapter import get_adapter


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

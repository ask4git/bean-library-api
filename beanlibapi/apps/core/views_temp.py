import json

from django.core import serializers
from django.http import JsonResponse

from beanlibapi.apps.authx.jwt_temp import (
    authenticate_jwt,
)
from .models import Bean


def protected_view(request):
    user = authenticate_jwt(request)

    if request.method == "GET":
        if user is None:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        beans = Bean.objects.all()
        data = serializers.serialize('json', beans)
        return JsonResponse(json.loads(data), safe=False, status=200)

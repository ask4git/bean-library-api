import json

from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from .jwt_temp import (
    generated_jwt_token,
    generate_jwt_token_payload,
    authenticate_jwt,
)
from .models import Bean


@csrf_exempt
def login_view(request):
    headers = {"content_type": "application/json"}

    if request.method == 'POST':
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, headers=headers, status=400)

        username = body.get('username')
        password = body.get('password')

        if not username or not password:
            return JsonResponse({"error": "Missing username or password"}, headers=headers, status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                payload = generate_jwt_token_payload(user)
                token = generated_jwt_token(payload)

                headers.update({"Authorization": f"Bearer {token}"})
                return JsonResponse(
                    data={
                        "expire": payload.get("expire"),
                        "token": token
                    },
                    headers=headers,
                    status=200
                )
        else:
            payload = {"error": "Login failed"}
            return JsonResponse(payload, headers=headers, status=401)


def protected_view(request):
    user = authenticate_jwt(request)

    if request.method == "GET":
        if user is None:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        beans = Bean.objects.all()
        data = serializers.serialize('json', beans)
        return JsonResponse(json.loads(data), safe=False, status=200)

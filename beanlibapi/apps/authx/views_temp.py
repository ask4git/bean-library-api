import json

from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from .jwt_temp import (
    generated_jwt_token,
    generate_jwt_token_payload,
)


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

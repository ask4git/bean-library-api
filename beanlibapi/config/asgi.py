"""
ASGI config for beanlibapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Todo 환경변수 변경
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beanlibapi.config.settings.base')

application = get_asgi_application()

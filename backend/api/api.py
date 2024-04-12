# api/django-api.py

from django.core.handlers.asgi import ASGIRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.conf import settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django_application = WSGIRequest(ASGIRequest({'type': 'http', 'method': 'GET'}))

def handler(request, context):
    django_response = django_application(request)
    response = {
        "statusCode": django_response.status_code,
        "body": django_response.content.decode('utf-8'),
        "headers": dict(django_response.items())
    }
    return response

import json
from django.http import JsonResponse

def json_response(data, status=200):
    return JsonResponse(data, status=status, safe=False)


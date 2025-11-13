from functools import wraps
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

def token_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return JsonResponse({'message': 'Authentication token missing or invalid format'}, status=401)

        try:
            token = Token.objects.get(key=token)
            request.user = token.user
        except Token.DoesNotExist:
            return JsonResponse({'message': 'Invalid token'}, status=401)
        except Exception as e:
            return JsonResponse({'message': f'Token validation error: {str(e)}'}, status=500)
        
        return view_func(request, *args, **kwargs)
    return wrapper
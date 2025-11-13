from django.views import View
from .utils import json_response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.forms.models import model_to_dict
from .models import *
from .decorators import token_required
from django.utils.decorators import method_decorator
from .forms import *
import json
import pdb

class RegisterView(View):
    def post(self,request):
        try:
            req_data = json.loads(request.body)
            form = RegisterForm(req_data)
            if form.is_valid():
                user = form.save()
                new_user = model_to_dict(user)
                data = {
                    "msg":"Registration completed. Please login.",
                    "user":new_user
                }
                return json_response(data, status=201)
            else:
                data = {
                    "error":"Invalid or missing details.",
                }
                return json_response(data, status=401)
        except Exception as e:
            data = {
                "error":str(e)
            }
            return json_response(data, status=500)

class LoginView(View):
    def post(self, request):
        try:
            token=None
            data = json.loads(request.body)
            username=data.get('username')
            password=data.get('password')
            user=User.objects.get(username=username,password=password)
            if user is not None:
                token = Token.objects.create(user=user)
                request.user = token.user
                data = {
                    "msg":f"Welcome, {username}!",
                    "token":token.key
                }
                return json_response(data)
            else:
                data = {
                    "error":"User not found!"
                }
                return json_response(data,status=404)
        except Exception as e:
            data = {
                "error":str(e)
            }
            return json_response(data, status=500)

class LogoutView(View):
    @method_decorator(token_required)
    def post(self, request):
        try:
            token = request.headers.get('Authorization')
            Token.objects.get(key=token).delete()
            data = {
            'msg': 'You are logged out.'
            }
            return json_response(data)
        except Exception as e:
            data = {
                "error":str(e)
            }
            return json_response(data, status=500)

class CategoryView(View):
    @method_decorator(token_required)
    def get(self, request):
        try:
            category = Category.objects.all().values()
            cat_list = list(category)
            data = {
                "msg":"Successfull.",
                "Catagory":cat_list
            }
            return json_response(data)
        except Exception as e:
            data = {
                "error":str(e)
            }
            return json_response(data, status=500)

    @method_decorator(token_required)
    def post(self, request):
        try:
            req_data = json.loads(request.body)
            form = CategoryForm(req_data)
            if form.is_valid():
                category = form.save()
                new_category = model_to_dict(category)
                data = {
                    "msg":"New category created.",
                    "Category":new_category
                }
                return json_response(data, status=201)
            else:
                data = {
                    "error":"Invalid or missing details.",
                }
                return json_response(data, status=401)
            
        except Exception as e:
            data = {
                "error":str(e)
            }
            return json_response(data, status=500)

    @method_decorator(token_required)
    def delete(self, request):
        category = None
        try:
            req_data = json.loads(request.body)
            category = Category.objects.get(id=req_data.get('id'))
        except Category.DoesNotExist:
            data = {
                "error":"Category does not exist!"
                }
            return json_response(data,status=404)
        try:
            category.delete()
            data = {
                "msg":"Category deleted."
            }
            return json_response(data)
        except Exception as e:
            data = {
                "error":str(e)
            }
            return json_response(data, status=500)

    @method_decorator(token_required)
    def put(self, request):
        category = None
        try:
            req_data = json.loads(request.body)
            try:
                category = Category.objects.get(id=req_data.get('id'))
            except Category.DoesNotExist:
                data = {
                    "error":"Category does not exist!"
                    }
                return json_response(data,status=404)
            form = CategoryForm(req_data, instance=category)
            if form.is_valid():
                update_category = form.save()
                updated_category = model_to_dict(update_category)
                data = {
                    "msg":"Category updated.",
                    "Category":updated_category
                }
                return json_response(data)
            else:
                data = {
                    "error":"Invalid or missing details.",
                }
                return json_response(data, status=401)

        except Exception as e:
            data = {
                "error":str(e)
            }
            return json_response(data, status=500)
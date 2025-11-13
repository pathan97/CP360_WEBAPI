from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/',csrf_exempt(RegisterView.as_view()),name='register'),
    path('login/',csrf_exempt(LoginView.as_view()),name='login'),
    path('logout/',csrf_exempt(LogoutView.as_view()),name='logout'),
    path('category/',csrf_exempt(CategoryView.as_view()),name='category')
]
from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/',csrf_exempt(RegisterView.as_view()),name='register'),
    path('login/',csrf_exempt(LoginView.as_view()),name='login'),
    path('logout/',csrf_exempt(LogoutView.as_view()),name='logout'),
    path('category/',csrf_exempt(CategoryView.as_view()),name='category'),
    path('product/',csrf_exempt(ProductView.as_view()),name='product'),
    path('dummy_cat_prod/',csrf_exempt(generate_dummy_category_product.as_view()),name='generate_dummy_category_product')
]
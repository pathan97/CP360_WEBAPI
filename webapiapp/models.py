from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=20,null=False,blank=False)

    class Meta:
        verbose_name_plural = 'User'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.name

class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=False,blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=15, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.name
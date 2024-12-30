from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=64)
    image_url = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    publication_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    publication_date = models.DateField(auto_now=True)
    is_sold = models.BooleanField(default=False)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True, related_name="category")
    
    def __str__(self):
        return f"{self.title}"
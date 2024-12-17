from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    # image = models.ImageField()
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    publication_date = models.DateField()

    def __str__(self):
        return f"{self.title} Price: {self.price} {self.currency} {self.publication_date}"

class Bid(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')

     def __str__(self):
        return f"Price: {self.price} {self.currency}"

# class Comments(models.Model):
#     return
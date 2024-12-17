from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    # image = models.ImageField()
    title = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    publication_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title} Price: {self.price} {self.currency} {self.publication_date}"

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bid')
    user = models.ForeignKey(User.first_name, on_delete=models.CASCADE, related_query_name='bid')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')

    class Meta:
        ordering = ('bid_time',) # Most recent bid first

    def __str__(self):
        return f"Bid of : {self.price} {self.currency} by {self.user.first_name}"

# class Comments(models.Model):
#     return
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

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
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="listings")
    created_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", default=6)
    
    def __str__(self):
        return f"""
    {self.title}
    Description: {self.description}
    Price: {self.price}$ 
    {self.image_url} 
    """

class Watchlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='watchlist')
    listings = models.ManyToManyField(Listing, related_name='watchlists')

    def __str__(self):
        return f"{self.user.username}'s Watchlist"

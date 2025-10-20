from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
     

class Listing(models.Model):
    title = models.CharField(max_length=64)
    image_url = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null= True, related_name="listings")
    created_at = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", null=True, blank=True)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_available = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="won_listing")
    
    
    def __str__(self):
        return f"""
    {self.title}
    Description: {self.description}
    Price: {self.price}$ 
    {self.image_url} 
    Created_by: {self.created_by}
    """

class Watchlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='watchlist')
    listings = models.ManyToManyField(Listing, related_name='watchlists')

    def __str__(self):
        return f"{self.user.username}'s Watchlist"

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bids")
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"""
    {self.user.username}
    bid ${self.bid_amount} on {self.listing.title} by {self.user.username} on {self.timestamp}
    """   

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_user")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comment")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

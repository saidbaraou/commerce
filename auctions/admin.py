from django.contrib import admin
from .models import User, Listing, Bid, Description, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Description)
admin.site.register(Category)
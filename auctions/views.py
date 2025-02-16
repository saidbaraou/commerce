from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing
from .forms import AddListingForm, CategoryFilterForm


def index(request):
    listings = Listing.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, "auctions/index.html", {
        "listings": listings,
        "categories": categories
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def create_listing_view(request):
    if request.method == "POST":
        form = AddListingForm(request.POST)
        if form.is_valid():
                new_listing = form.save()
                return HttpResponseRedirect(reverse("index"))
    else: form = AddListingForm()

    context = {
        "form": form,
        "title": "New listing"
    }
    return render(request, "auctions/create-listing.html", context)


def filter_category_view(request):
    form = CategoryFilterForm()
    available_listings = Listing.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if request.method == 'GET':
        selected_category = request.GET.get('category')
        print(selected_category)
        listings = available_listings.filter(category__name=selected_category)
        print(listings)
         
    context = {
        "form": form,
        "categories": categories,
        "listings": listings
    }
    return render(request, 'auctions/index.html', context)

def watchlist_view(request):
    form = CategoryFilterForm()
    available_listings = Listing.objects.filter(is_sold=False)
    categories = Category.objects.all()
    if request.method == 'GET':
        selected_category = request.GET.get('category')
        print(selected_category)
        listings = available_listings.filter(category__name=selected_category)
        print(listings)
        
    context = {
        "form": form,
        "categories": categories,
        "listings": listings
    }
    
    return render(request, 'auctions/index.html', context)
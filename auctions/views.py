from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Category, Listing
from .forms import AddListingForm, CategoryFilterForm


def index(request):
    listings = Listing.objects.filter(is_sold=False)
    categories = Category.objects.all()

    context = {
        "listings": listings,
        "categories": categories
    }

    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        context = {
            "message": "Invalid username and/or password."
        }

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", context)
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


def listing_detail_view(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    is_in_watchlist = request.user in listing.watchlist.all()
    context = {
        "listing": listing,
        "is_in_watchlist": is_in_watchlist
        }
    return render(request, 'auctions/listing_detail.html', context)

def add_watchlist_view(request, id):
    listing = Listing.objects.get(pk=id)
    user = request.user
    listing.watchlist.add(user)
    return HttpResponseRedirect(reverse("listing_detail",args=(id, )))

def remove_watchlist_view(request, id):
    listing = Listing.objects.get(pk=id)
    user = request.user
    listing.watchlist.remove(user)
    return HttpResponseRedirect(reverse("listing_detail", args=(id, )))
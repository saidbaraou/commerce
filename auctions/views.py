from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import User, Category, Listing, Watchlist
from .forms import AddListingForm, CategoryFilterForm, BidForm


def index(request):
    if request.user.is_authenticated:
        return welcome_view(request)
    else:
        return home_view(request)

def home_view(request):
    """View for logged-out users"""
    listings = Listing.objects.filter(is_sold=False)
    categories = Category.objects.all()

    context = {
        "listings": listings,
        "categories": categories,
    }

    return render(request, 'auctions/home.html', context)

@login_required
def welcome_view(request):
    """View for logged-in users"""
    listings = Listing.objects.filter(is_sold=False)
    categories = Category.objects.all()
    user = request.user
    watchlist_number = get_watchlist_length(user)

    context = {
        "listings": listings,
        "categories": categories,
         "watchlist_number": watchlist_number
    }

    return render(request, 'auctions/welcome.html', context)



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
    user = request.user
    watchlist_number = get_watchlist_length(user)

    if request.method == "POST":
        form = AddListingForm(request.POST)
        if form.is_valid():
                new_listing = form.save()
                return HttpResponseRedirect(reverse("index"))
    else: form = AddListingForm()

    context = {
        "form": form,
        "title": "New listing",
        "watchlist_number": watchlist_number
    }
    return render(request, "auctions/create-listing.html", context)


def filter_category_view(request):
    form = CategoryFilterForm()
    available_listings = Listing.objects.filter(is_sold=False)
    categories = Category.objects.all()

    if request.method == 'GET':
        
        selected_category = request.GET.get('category')
        
        if selected_category != "all":
            listings = available_listings.filter(category__name=selected_category)
        else:
            listings = available_listings

    context = {
        "form": form,
        "categories": categories,
        "listings": listings
    }
    return render(request, 'auctions/index.html', context)


def get_watchlist_listing(user):

    try:
        watchlist = Watchlist.objects.get(user=user)
        listings = watchlist.listings.all()
        return listings
    except Watchlist.DoesNotExist:
        message = "There's no listing in your watchlist"
        return message
    
    
def get_watchlist_length(user):

    try:
        watchlist = Watchlist.objects.get(user=user)
        watchlist_number = watchlist.listings.count()
        return watchlist_number
    except Watchlist.DoesNotExist:
        watchlist_number = 0
        return watchlist_number
    
def watchlist_view(request):
    user = request.user
    watchlist_listings = get_watchlist_listing(user)

    watchlist_number = get_watchlist_length(user)
    context = {
        "watchlist_listings": watchlist_listings,
        "watchlist_number": watchlist_number
    }
    return render(request, "auctions/watchlist.html", context)


def listing_detail_view(request, listing_id):
    
    listing = get_object_or_404(Listing, pk=listing_id)
    is_in_watchlist = False

    if request.user.is_authenticated:
        user = request.user
        watchlist_number = get_watchlist_length(user)
        try:
            watchlist = Watchlist.objects.get(user=request.user)
            is_in_watchlist = listing in watchlist.listings.all()
        except Watchlist.DoesNotExist:
            pass

    context = {
        "listing": listing,
        "is_in_watchlist": is_in_watchlist,
        "watchlist_number": watchlist_number
        }
    return render(request, 'auctions/listing_detail.html', context)

@login_required
def add_watchlist_view(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    user = request.user
    #get or create the watchlist
    watchlist, created = Watchlist.objects.get_or_create(user=user)
    #add the listing to the watchlist 
    watchlist.listings.add(listing) 
    return HttpResponseRedirect(reverse("watchlist"))

@login_required
def remove_watchlist_view(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    user = request.user
    #get or create the watchlist
    watchlist, created = Watchlist.objects.get_or_create(user=user)
    #remove the listing from the watchlist 
    watchlist.listings.remove(listing) 
    return HttpResponseRedirect(reverse("watchlist"))


@login_required
def place_bid(request):
    user = request.user
    watchlist_number = get_watchlist_length(user)

    if request.method == "POST":
        form = BidForm(request.POST)
        if form.is_valid():
                new_bid = form.save()
                return HttpResponseRedirect(reverse("listing-detail"))
    else: form = BidForm()

    context = {
        "form": form,
        "title": "New Listing",
        "watchlist_number": watchlist_number
    }
    return render(request, "auctions/listing-detail.html", context)

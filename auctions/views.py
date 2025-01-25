from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing
from .forms import AddListingForm


def index(request):
    all_categories = Category.objects.all()
    all_listings = Listing.objects.filter(is_sold=False)
    return render(request, "auctions/index.html", {
        "all_categories": all_categories,
        "all_listings": all_listings
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
            print("Form is VALID!")
            print(form.cleaned_data) # Check the cleaned data
            try:
                new_listing = form.save()
                return HttpResponseRedirect(reverse("index"))
            except Exception as e:
                print(f"Error saving: {e}") # Print any exceptions during save
        else:
            print("Form is NOT valid!")
            print(form.errors) # EXAMINE THESE ERRORS CAREFULLY!!!
    else: form = AddListingForm()
    return render(request, "auctions/create-listing.html", {
        "form": form,
        "title": 'New listing',
    })
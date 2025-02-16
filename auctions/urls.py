from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create-listing", views.create_listing_view, name="create_listing"),
    path("filter-category", views.filter_category_view, name="filter_category"),
    path("watchlist", views.watchlist_view, name="watchlist")
]

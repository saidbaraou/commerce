from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create-listing", views.create_listing_view, name="create_listing"),
    path("filter-category", views.filter_category_view, name="filter_category"),
    path('listing-detail/<int:listing_id>/', views.listing_detail_view, name='listing_detail'),
    path("watchlist", views.watchlist_view, name="watchlist"),
    path("add-watchlist/<int:id>", views.add_watchlist_view, name="add_watchlist"),
    path("remove-watchlist/<int:id>", views.remove_watchlist_view, name="remove_watchlist")
]

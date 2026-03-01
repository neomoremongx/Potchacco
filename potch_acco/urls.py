from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_home, name="get_home"),
    path("providers", views.get_rental_provider, name="get_rental_provider"),
    path("about", views.get_about, name="get_about"),
    path("contact", views.get_contact, name="get_contact"),
    path("listing", views.get_listed, name="get_listed"),
    path("profile", views.get_profile, name="get_profile"),
    path("trust", views.get_t_and_s, name="get_t_and_s"),
    path("terms", views.get_ts_cs, name="get_ts_cs")
]
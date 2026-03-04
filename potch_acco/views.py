from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def get_home(request):

    return render(request, "home.html")

def get_rental_provider(request):

    return render(request, "provider.html")

def get_about(request):

    return render(request, "about.html")

def get_contact(request):

    return render(request, "contact.html")

def get_listed(request):

    return render(request, "listing.html")

def get_profile(request):

    return render(request, "profile.html")

def get_ts_cs(request):

    return render(request, "ts_cs.html")

def get_t_and_s(request):

    return render(request, "trust_safety.html")

def get_specific_category(request):

    return render(request, "list_by_category.html")

def get_pricing(request):

    return render(request, "pricing.html")

def get_property(request):

    return render(request, "property.html")




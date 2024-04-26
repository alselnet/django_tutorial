from django.http.response import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listings

def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", { "bands":bands })

def about(request):
	return render(request, "listings/about.html")

def listings(request):
    listings = Listings.objects.all()
    return render(request, "listings/listings.html", {"listings":listings})

def contact_us(request):
	return render(request, "listings/contact_us.html")
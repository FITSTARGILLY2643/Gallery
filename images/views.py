from django.shortcuts import render,redirect
from .models import Location,Category,Image
from django.http import HttpResponse, Http404
import datetime as dt
# Create your views here.
def index(request):
    return render(request,'index.html')

def gallery(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'gallery.html', {"date": date,"images":images})

def search_location(request):
    if 'location' in request.GET and request.GET["location"]:
        location = request.GET.get("location")
        searched_images = Image.filter_by_location(location)
        message = f"{location}"
        return render(request, 'location.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image"
        return render(request, 'location.html', {"message": message})

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        return render(request, 'category.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image"
        return render(request, 'category.html', {"message": message})



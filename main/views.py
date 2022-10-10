from multiprocessing import context
from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    data = { 
        "name": "Home Page",
        "xyz": 123
    }
    
    return render(request, "main/index.html", data)


def about(request):
    context = {
        "places": ["patna", "gaya", "madhubani"],
        "name": "About Page"
    }
    return render(request, "main/about.html", context)
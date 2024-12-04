from django.shortcuts import render
from .models import ServiceCard

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request, "about.html")

def skills(request):
    return render(request , "skills.html")

def service(request):
    cards = ServiceCard.objects.all()
    return render(request, "service.html" , {'cards': cards})

def contact(request):
    return render(request, "contact.html")
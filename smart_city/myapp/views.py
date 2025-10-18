from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):        return render(request, 'myapp/home.html')
def About(request):       return render(request, 'myapp/about.html')
def Booking(request):     return render(request, 'myapp/booking.html')
def Contact(request):     return render(request, 'myapp/contact.html')
def Menu(request):        return render(request, 'myapp/menu.html')
def Service(request):     return render(request, 'myapp/service.html')
def Team(request):        return render(request, 'myapp/team.html')
def Testimonial(request): return render(request, 'myapp/testimonial.html')
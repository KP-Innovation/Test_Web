from django.urls import path
from .views import Home, About, Booking, Contact, Menu, Service, Team, Testimonial

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('booking/', Booking, name='booking'),
    path('contact/', Contact, name='contact'),
    path('menu/', Menu, name='menu'),
    path('service/', Service, name='service'),
    path('team/', Team, name='team'),
    path('testimonial/', Testimonial, name='testimonial'),
]

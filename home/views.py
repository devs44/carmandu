from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.



class HomeView(TemplateView):
    template_name = 'home/base/index.html'

class Carview(TemplateView):
    template_name = 'home/cars/cars.html'

class AboutView(TemplateView):
    template_name = 'home/about/about.html'

class ServiceView(TemplateView):
    template_name = 'home/services/services.html'

class ContactView(TemplateView):
    template_name = 'home/contact/contact.html'

from django.urls import path
from . import views
from .views import *

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('cars/', Carview.as_view(), name='cars'),
    path('about/',  AboutView.as_view(), name='about'),
    path('services/',  ServiceView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
]


from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', DashboardView.as_view(), name='index'),
]

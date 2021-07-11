
from django.urls import path
from . import views
from .views import *

app_name = 'dashboard'
urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),

    # Brand
    path('dashboard/brand/list/', BrandListView.as_view(), name='brands'),
    path('dashboard/brand/create/', BrandCreateView.as_view(), name='brand-create'),
    path('dashboard/brand/<int:pk>/update/',
         BrandUpdateView.as_view(), name='brand-update'),
    path('dashboard/brand/<int:pk>/delete/', BrandDeleteView.as_view(), name='brand-delete'),

    # model
    path('dashboard/model/list/', ModelListView.as_view(), name='models'),
    path('dashboard/model/create/', ModelCreateView.as_view(), name='model-create'),
    path('dashboard/model/<int:pk>/update/',
             ModelUpdateView.as_view(), name='model-update'),
    path('dashboard/model/<int:pk>/delete/', ModelDeleteView.as_view(), name='model-delete'),

    # Cars
    path('dashboard/cars/list/', CarListView.as_view(), name='cars'),
    path('dashboard/cars/create/', CarCreateView.as_view(), name='cars-create'),
    path('dashboard/cars/<int:pk>/update/',
         CarUpdateView.as_view(), name='cars-update'),
    path('dashboard/cars/<int:pk>/delete/', CarDeleteView.as_view(), name='cars-delete'),
]

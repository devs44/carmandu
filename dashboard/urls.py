
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

    # type
    path('dashboard/type/list/', TypeListView.as_view(), name='types'),
    path('dashboard/type/create/',  TypeCreateView.as_view(), name='type-create'),
    path('dashboard/type/<int:pk>/update/',
              TypeUpdateView.as_view(), name='type-update'),
    path('dashboard/type/<int:pk>/delete/',  TypeDeleteView.as_view(), name='type-delete'),

    # category
    path('dashboard/category/list/', CategoryListView.as_view(), name='categories'),
    path('dashboard/category/create/',  CategoryCreateView.as_view(), name='category-create'),
    path('dashboard/category/<int:pk>/update/',
              CategoryUpdateView.as_view(), name='category-update'),
    path('dashboard/category/<int:pk>/delete/',  CategoryDeleteView.as_view(), name='category-delete'),

    # features
    path('dashboard/features/list/', FeatureListView.as_view(), name='features'),
    path('dashboard/features/create/',  FeatureCreateView.as_view(), name='feature-create'),
    path('dashboard/features/<int:pk>/update/',
              FeatureUpdateView.as_view(), name='feature-update'),
    path('dashboard/features/<int:pk>/delete/',  FeatureDeleteView.as_view(), name='feature-delete'),

    # Cars
    path('dashboard/cars/list/', CarListView.as_view(), name='cars'),
    path('dashboard/cars/create/', CarCreateView.as_view(), name='cars-create'),
    path('dashboard/cars/<int:pk>/update/',
         CarUpdateView.as_view(), name='cars-update'),
    path('dashboard/cars/<int:pk>/delete/', CarDeleteView.as_view(), name='cars-delete'),
    path('dashboard/cars/image/create/', CarImageCreateView.as_view(), name='cars-image-create'),

    # about
    path('dashboard/about/list/', AboutListView.as_view(), name='abouts'),
    path('dashboard/about/create/',  AboutCreateView.as_view(), name='about-create'),
    path('dashboard/about/<int:pk>/update/',
              AboutUpdateView.as_view(), name='about-update'),
    path('dashboard/about/<int:pk>/delete/',  AboutDeleteView.as_view(), name='about-delete'),

    # team
    path('dashboard/team/list/', TeamListView.as_view(), name='teams'),
    path('dashboard/team/create/',  TeamCreateView.as_view(), name='team-create'),
    path('dashboard/team/<int:pk>/update/',
              TeamUpdateView.as_view(), name='team-update'),
    path('dashboard/team/<int:pk>/delete/',  TeamtDeleteView.as_view(), name='team-delete'),

    # services
    path('dashboard/services/list/', ServiceListView.as_view(), name='services'),
    path('dashboard/services/create/',  ServiceCreateView.as_view(), name='service-create'),
    path('dashboard/services/<int:pk>/update/',
              ServiceUpdateView.as_view(), name='service-update'),
    path('dashboard/services/<int:pk>/delete/',  ServiceDeleteView.as_view(), name='service-delete'),


    # services video
    path('dashboard/services-video/list/', ServiceVideoListView.as_view(), name='services-video'),
    path('dashboard/services-video/create/',  ServiceVideoCreateView.as_view(), name='service-video-create'),
    path('dashboard/services-video/<int:pk>/update/',
              ServiceVideoUpdateView.as_view(), name='service-video-update'),
    path('dashboard/services-video/<int:pk>/delete/',  ServiceVideoDeleteView.as_view(), name='service-video-delete'),

    # contact
    path('dashboard/contact/list/', ContactListView.as_view(), name='contacts'),
    path('dashboard/contact/create/',  ContactCreateView.as_view(), name='contact-create'),
    path('dashboard/contact/<int:pk>/update/',
              ContactUpdateView.as_view(), name='contact-update'),
    path('dashboard/contact/<int:pk>/delete/',  ContactDeleteView.as_view(), name='contact-delete'),

]

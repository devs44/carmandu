
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *
from .forms import *
from .mixins import *
# Create your views here.

class DashboardView(TemplateView):
    template_name = 'dashboard/base/index.html'

# brands
class BrandListView(NonDeletedListMixin,ListView):
    template_name = 'dashboard/brand/list.html'
    model = Brand

    def get_queryset(self):
        queryset = super().get_queryset()
        if "title" in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    name__contains=self.request.GET.get("title"))
        return queryset


class BrandCreateView(CreateView):
    template_name = 'dashboard/brand/form.html'
    form_class = BrandForm
    success_url = reverse_lazy('dashboard:brands')


class BrandUpdateView(UpdateView):
    template_name = 'dashboard/brand/form.html'
    model = Brand
    form_class = BrandForm
    success_url = reverse_lazy('dashboard:brands')


class BrandDeleteView(DeleteMixin, DeleteView):
    model = Brand
    success_url = reverse_lazy('dashboard:brands')


# models
class ModelListView(NonDeletedListMixin,ListView):
    template_name = 'dashboard/model/list.html'
    model = Model

    def get_queryset(self):
        queryset = super().get_queryset()
        if "title" in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    name__contains=self.request.GET.get("title"))
        return queryset


class ModelCreateView(CreateView):
    template_name = 'dashboard/model/form.html'
    form_class = ModelForm
    success_url = reverse_lazy('dashboard:models')


class ModelUpdateView(UpdateView):
    template_name = 'dashboard/model/form.html'
    model = Model
    form_class = ModelForm
    success_url = reverse_lazy('dashboard:models')


class ModelDeleteView(DeleteMixin,DeleteView):
    model = Model
    success_url = reverse_lazy('dashboard:models')


# types
class TypeListView(NonDeletedListMixin,ListView):
    template_name = 'dashboard/type/list.html'
    model = Type

    def get_queryset(self):
        queryset = super().get_queryset()
        if "title" in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    name__contains=self.request.GET.get("title"))
        return queryset


class TypeCreateView(CreateView):
    template_name = 'dashboard/type/form.html'
    form_class = TypeForm
    success_url = reverse_lazy('dashboard:types')


class TypeUpdateView(UpdateView):
    template_name = 'dashboard/type/form.html'
    model = Type
    form_class = TypeForm
    success_url = reverse_lazy('dashboard:types')


class TypeDeleteView(DeleteMixin,DeleteView):
    model = Type
    success_url = reverse_lazy('dashboard:types')

# category
class CategoryListView(NonDeletedListMixin,ListView):
    template_name = 'dashboard/category/list.html'
    model = Category

    def get_queryset(self):
        queryset = super().get_queryset()
        if "title" in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    name__contains=self.request.GET.get("title"))
        return queryset


class CategoryCreateView(CreateView):
    template_name = 'dashboard/category/form.html'
    form_class = CategoryForm
    success_url = reverse_lazy('dashboard:categories')


class CategoryUpdateView(UpdateView):
    template_name = 'dashboard/category/form.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('dashboard:categories')


class CategoryDeleteView(DeleteMixin,DeleteView):
    model = Category
    success_url = reverse_lazy('dashboard:categories')

# features
class FeatureListView(NonDeletedListMixin,ListView):
    template_name = 'dashboard/features/list.html'
    model = Features

    def get_queryset(self):
        queryset = super().get_queryset()
        if "title" in self.request.GET:
            if self.request.GET.get('title') != '':
                queryset = queryset.filter(
                    name__contains=self.request.GET.get("title"))
        return queryset


class FeatureCreateView(CreateView):
    template_name = 'dashboard/features/form.html'
    form_class = FeatureForm
    success_url = reverse_lazy('dashboard:features')


class FeatureUpdateView(UpdateView):
    template_name = 'dashboard/features/form.html'
    model = Features
    form_class = FeatureForm
    success_url = reverse_lazy('dashboard:features')


class FeatureDeleteView(DeleteMixin,DeleteView):
    model = Features
    success_url = reverse_lazy('dashboard:features')

# cars
class CarListView(NonDeletedListMixin,ListView):
    template_name = 'dashboard/cars/list.html'
    model = Car

    def get_queryset(self):
        queryset = super().get_queryset()
        if "name" in self.request.GET:
            if self.request.GET.get('name') != '':
                queryset = queryset.filter(
                    name__contains=self.request.GET.get("name"))
        return queryset

class CarImageCreateView(CreateView):
    model = CarImage
    form_class = CarImageForm
    template_name = "dashboard/car/imageform.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.is_ajax():
            return super().dispatch(request, *args, **kwargs)
        return JsonResponse({"error": "Cannot access this page"}, status=404)

    def form_valid(self, form):
        instance = form.save()
        return JsonResponse(
            {
                "status": "ok",
                "pk": instance.pk,
                "url": instance.image.url,
            }
        )

    def form_invalid(self, form):
        return JsonResponse({"errors": form.errors}, status=400)

class CarCreateView(CreateView):
    template_name = 'dashboard/cars/form.html'
    form_class = CarForm
    success_url = reverse_lazy('dashboard:cars')


class CarUpdateView(UpdateView):
    template_name = 'dashboard/cars/form.html'
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('dashboard:cars')


class CarDeleteView(DeleteMixin, DeleteView):
    model = Car
    success_url = reverse_lazy('dashboard:cars')

# abouts
class AboutListView(NonDeletedListMixin,ListView):
    template_name = 'dashboard/about/list.html'
    model = About


class AboutCreateView(CreateView):
    template_name = 'dashboard/about/form.html'
    form_class = AboutForm
    success_url = reverse_lazy('dashboard:abouts')


class AboutUpdateView(UpdateView):
    template_name = 'dashboard/about/form.html'
    model = About
    form_class = AboutForm
    success_url = reverse_lazy('dashboard:abouts')


class AboutDeleteView(DeleteMixin,DeleteView):
    model = About
    success_url = reverse_lazy('dashboard:abouts')

# teams
class TeamListView(NonDeletedListMixin,ListView):
    template_name = 'dashboard/team/list.html'
    model = Team


class TeamCreateView(CreateView):
    template_name = 'dashboard/team/form.html'
    form_class = TeamForm
    success_url = reverse_lazy('dashboard:teams')


class TeamUpdateView(UpdateView):
    template_name = 'dashboard/team/form.html'
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('dashboard:teams')


class TeamtDeleteView(DeleteMixin,DeleteView):
    model = Team
    success_url = reverse_lazy('dashboard:teams')

# services
class ServiceListView(NonDeletedListMixin,ListView):
    template_name = 'dashboard/services/list.html'
    model = Services


class ServiceCreateView(CreateView):
    template_name = 'dashboard/services/form.html'
    form_class = ServicesForm
    success_url = reverse_lazy('dashboard:services')


class ServiceUpdateView(UpdateView):
    template_name = 'dashboard/services/form.html'
    model = Services
    form_class = ServicesForm
    success_url = reverse_lazy('dashboard:services')


class ServiceDeleteView(DeleteMixin,DeleteView):
    model = Services
    success_url = reverse_lazy('dashboard:services')


# services-video
class ServiceVideoListView(NonDeletedListMixin,ListView):
    template_name = 'dashboard/services-video/list.html'
    model = ServicesVideo


class ServiceVideoCreateView(CreateView):
    template_name = 'dashboard/services-video/form.html'
    form_class = ServicesVideoForm
    success_url = reverse_lazy('dashboard:services-video')


class ServiceVideoUpdateView(UpdateView):
    template_name = 'dashboard/services-video/form.html'
    model = ServicesVideo
    form_class = ServicesVideoForm
    success_url = reverse_lazy('dashboard:services-video')


class ServiceVideoDeleteView(DeleteMixin,DeleteView):
    model = ServicesVideo
    success_url = reverse_lazy('dashboard:services-video')

# contact
class ContactListView(NonDeletedListMixin,ListView):
    template_name = 'dashboard/contact/list.html'
    model = Contact


class ContactCreateView(CreateView):
    template_name = 'dashboard/contact/form.html'
    form_class = ContactForm
    success_url = reverse_lazy('dashboard:contacts')


class ContactUpdateView(UpdateView):
    template_name = 'dashboard/contact/form.html'
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('dashboard:contacts')


class ContactDeleteView(DeleteMixin,DeleteView):
    model = Contact
    success_url = reverse_lazy('dashboard:contacts')
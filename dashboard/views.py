from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import *
from .forms import *
# Create your views here.

class DashboardView(TemplateView):
    template_name = 'dashboard/base/index.html'

# brands
class BrandListView(ListView):
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
# brands
class BrandListView(ListView):
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
# brands
class BrandListView(ListView):
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


# cars
class CarListView(ListView):
    template_name = 'dashboard/cars/list.html'
    model = Car

    def get_queryset(self):
        queryset = super().get_queryset()
        if "name" in self.request.GET:
            if self.request.GET.get('name') != '':
                queryset = queryset.filter(
                    name__contains=self.request.GET.get("name"))
        return queryset


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

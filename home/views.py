from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy

from dashboard.forms import MessageForm
from django.views.generic.edit import CreateView
from dashboard.models import Car, Team
from django.views.generic import TemplateView, ListView
# Create your views here.

from dashboard.models import Car, Team, About, ServicesVideo, Contact, Message

class HomeView(TemplateView):
    template_name = 'home/base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featuredcars'] = Car.objects.filter(is_featured=True, deleted_at__isnull=True)
        context['latestcars'] = Car.objects.order_by('-id')[:100]
        context['team'] = Team.objects.filter(deleted_at__isnull=True)
        return context

class Carview(ListView):
    template_name = 'home/cars/cars.html'
    model = Car
    context_object_name = 'cars'

class AboutView(TemplateView):
    template_name = 'home/about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.filter(deleted_at__isnull=True)
        context['team'] = Team.objects.filter(deleted_at__isnull=True)
        return context

class ServiceView(TemplateView):
    template_name = 'home/services/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicevideo'] = ServicesVideo.objects.filter(deleted_at__isnull=True)
        return context

class ContactView(CreateView):
    template_name = 'home/contact/contact.html'
    form_class = MessageForm
    success_url = reverse_lazy('home:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.filter(deleted_at__isnull=True)
        form = MessageForm(self.request.POST or None)
        context['form'] = MessageForm()

        return context

    def post(self, request, *args, **kwargs):
        full_name = request.POST.get('full_name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        obj = Message.objects.create(
            full_name=full_name, subject=subject, email=email, phone=phone, message=message)
        return redirect('home:contact')

    def form_valid(self, form):
        email = form.cleaned_data['email']

        if "@" not in email:
            return render(self.request, self.template_name,
                          {
                              'error': 'Invalid email',
                              'form': form
                          })
        else:
            pass
        return super().form_valid(form)
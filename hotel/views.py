from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserChangeForm
from .models import Hotel
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(TemplateView):
    http_method_names = ['get']
    template_name = 'hotel/homepage.html'
    model = Hotel

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        hotels = Hotel.objects.all().order_by('-id')[0:30]
        context['hotels'] = hotels
        return context

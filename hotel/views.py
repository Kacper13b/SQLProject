from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserChangeForm
from .models import Hotel, Room
from django.contrib.auth.mixins import LoginRequiredMixin
from customer.models import *
from .forms import ReservationForm, CustomerForm



# def get_children_recursive(parent_category):
#     children = parent_category.children.all()  # This depends on adding related_name to Category
#     for child in children:
#         children += get_children_recursive(child)
#     return children

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


class HotelPage(ListView):
    http_method_names = ['get']
    template_name = 'hotel/rooms.html'
    model = Room
    slug_field = 'id'
    slug_url_kwarg = 'id'

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)


    def get_queryset(self):
        hotels = []
        hotel = Hotel.objects.get(id=self.kwargs['pk'])
        hotels.append(hotel)
        return hotels[0].rooms.all()
        
        

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        rooms = self.get_queryset()
        rooms_new = rooms.filter(availability=True)
        context['rooms'] = rooms_new
        return context


class ReservationView(FormView):
    model = Room
    template_name = 'hotel/reservation.html'
    form_class = ReservationForm
    success_url = '/'

    def get_queryset(self):
        
        room = Room.objects.get(id=self.kwargs['pk'])
        return room

    def form_valid(self, form):
        form.save()
        room = self.get_queryset()
        room.availability = False
        room.save()
        return super().form_valid(form)

class CustomerView(FormView):
    template_name = 'hotel/customer.html'
    form_class = CustomerForm
    success_url = '/'

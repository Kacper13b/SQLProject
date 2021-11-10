from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.forms import UserChangeForm
from .models import Hotel, Room
from django.contrib.auth.mixins import LoginRequiredMixin
from customer.models import *
from .forms import ReservationForm, CustomerForm, UserForm
from django.http import Http404
from django.shortcuts import render


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


# class ReservationView(FormView):
#     model = Room
#     template_name = 'hotel/reservation.html'
#     form_class = ReservationForm
#     success_url = '/reservation/customer'

#     def get_queryset(self):       
#         room = Room.objects.get(id=self.kwargs['pk'])
#         return room

#     def form_valid(self, form):
#         form.save()
#         room = self.get_queryset()
#         #room.availability = False
#         #room.reservation = form.save()
#         room.save()
#         return super().form_valid(form)

# class CustomerView(FormView):
#     model = Room
#     form_class = CustomerForm
#     template_name = 'hotel/customer.html'
#     success_url = '/'

#     def get_queryset(self):      
#         #room = ReservationView.get_queryset(ReservationView)
#         room = Room.objects.get(id=self.kwargs['pk'])
#         return room


#     def form_valid(self, form):
#         form.save()
#         room = self.get_queryset()
#         room.customer = form.save()
#         room.save()
#         return super().form_valid(form)


class FormView(FormView):
    template_name = 'hotel/test.html'
    success_url = '/'

    def get_object(self):
        try:
            obj = Room.objects.get(id=self.kwargs['pk'])
        except Room.DoesNotExist:
            raise Http404('Question not found!')
        return obj

    def get_customer(self):
        customer = Customer.objects.get(user=self.request.user)
        return customer

    def get_context_data(self, **kwargs):
        kwargs['room'] = self.get_object()
        if 'reservation_form' not in kwargs:
            kwargs['reservation_form'] = ReservationForm()
        if 'customer_form' not in kwargs:
            kwargs['customer_form'] = CustomerForm()
        if 'user_form' not in kwargs:
            kwargs['user_form'] = UserForm()

        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


    def post(self, request, *args, **kwargs):
        reservation_form = ReservationForm(request.POST)
        customer_form = CustomerForm(request.POST, instance=self.get_customer())
        user_form = UserForm(request.POST, instance=self.request.user)
        ctxt = {}
        print(reservation_form.is_valid())
        print(customer_form.is_valid())
        print(user_form.is_valid())
        #customer_form.user = self.request.user
        if reservation_form.is_valid() and customer_form.is_valid() and user_form.is_valid():
            reservation_form.save()
            #customer_form.user = self.request.user
            user_form.save()
            customer_form.save()
            room = self.get_object()
            room.availability = False
            room.reservation = reservation_form.save()
            room.user = user_form.save()
            room.save()
            
            return super().form_valid(reservation_form)
        else:
            ctxt['reservation_form'] = reservation_form
            ctxt['customer_form'] = customer_form
            ctxt['user_form'] = user_form

        return render(request, self.template_name, self.get_context_data(**ctxt))

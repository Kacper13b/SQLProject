from django.urls import path
from django.conf.urls import include, url
from . import views
app_name = "hotel"


urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('search_hotel', views.search_hotel, name='search_hotel'),
    # path('search_room', views.search_hotel, name='search_room'),
    path("<int:pk>/", views.HotelPage.as_view(), name='detail'),
    path("<int:pk>/reservation", views.FormView.as_view(), name='reservation'),
    path("my_reservations", views.MyReservationsView.as_view(), name='my_reservations'),
]
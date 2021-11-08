from django.urls import path
from django.conf.urls import include, url
from . import views
app_name = "hotel"


urlpatterns = [
    path("", views.HomePage.as_view(), name='index'),
    path("<int:pk>/", views.HotelPage.as_view(), name='detail'),
    path("<int:pk>/test", views.FormView.as_view(), name='test'),
]
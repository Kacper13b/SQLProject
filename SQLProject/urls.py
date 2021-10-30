
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url
from hotel import urls as hotel_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(hotel_urls, namespace='hotel')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

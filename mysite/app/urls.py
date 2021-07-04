from django.urls import path, admin
from django.conf.urls import url
from . views import index, nosotros, servicios, reservatuhora, contactanos, opinion



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('nosotros/', nosotros, name="nosotros"),
    path('servicios/', servicios, name="servicios"),
    path('reservatuhora/', reservatuhora, name="reservatuhora"),
    path('contactanos/', contactanos, name="contactanos"),
    path('opinion/', opinion, name="opinion"),




]
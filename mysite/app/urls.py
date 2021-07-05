from django.urls import path
from django.conf.urls import url
from . views import index, nosotros, servicios, cita, contactanos, opinion



urlpatterns = [
    
    path('', index, name="index"),
    path('nosotros/', nosotros, name="nosotros"),
    path('servicios/', servicios, name="servicios"),
    path('cita/', cita, name="cita"),
    path('contactanos/', contactanos, name="contactanos"),
    path('opinion/', opinion, name="opinion")




]
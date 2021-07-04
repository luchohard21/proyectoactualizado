from .models import Cita, Cliente, Club, DetalleCita, Detalle_Servicio, Detalle_servicio_empleado, Empleado, Especialidad, Pago, Tipo_servicio
from django.contrib import admin


# Register your models here.
#admin.site.register(Post)
admin.site.register(Cliente)
admin.site.register(Tipo_servicio)
admin.site.register(Empleado)
admin.site.register(DetalleCita)
admin.site.register(Cita)
admin.site.register(Detalle_Servicio)
admin.site.register(Pago)
admin.site.register(Club)
admin.site.register(Detalle_servicio_empleado)
admin.site.register(Especialidad)

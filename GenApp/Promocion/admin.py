from django.contrib import admin

# Register your models here.
from GenApp.Promocion.models import Motivo, Promocion

admin.site.register(Motivo)
admin.site.register(Promocion)

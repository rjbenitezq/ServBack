from django.contrib import admin

# Register your models here.
from GenApp.Privilegios.models import RolUser, Privilegios, Roles, Modulos, ModUser

admin.site.register(Modulos)
admin.site.register(ModUser)
admin.site.register(Roles)
admin.site.register(RolUser)
admin.site.register(Privilegios)
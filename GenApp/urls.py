from django.conf.urls import url
from django.urls import include

from GenApp.views import LoginView

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='rest_login'),
    url(r'^area/', include('GenApp.Area.urls')),
    url(r'^categoria/', include('GenApp.Categoria.urls')),
    url(r'^sucursal/', include('GenApp.Sucursal.urls')),
    url(r'^producto/', include('GenApp.Producto.urls')),
    url(r'^cliente/', include('GenApp.Cliente.urls')),

    url(r'^persona/', include('GenApp.Persona.urls')),
    url(r'^trabajador/', include('GenApp.Trabajador.urls')),
    url(r'^opciones/', include('GenApp.Privilegios.urls')),
    url(r'^promocion/', include('GenApp.Promocion.urls')),
]

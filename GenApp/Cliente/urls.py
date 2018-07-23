from django.conf.urls import url

from GenApp.Cliente import views

urlpatterns = [
    url(r'^listcliente/$', views.ListCliente.as_view()),
    url(r'^listcliente/(?P<pk>[0-9]+)/$', views.ListClienteDetail.as_view()),
    url(r'^clienteDetailApp/$', views.DataPersonalClienteApp.as_view()),

]

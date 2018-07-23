from django.conf.urls import url

from GenApp.Trabajador import views

urlpatterns = [
    url(r'^listrabajador/$', views.ListTrabajador.as_view()),
    url(r'^listrabajador/(?P<pk>[0-9]+)/$', views.ListTrabajadorDetail.as_view()),

]
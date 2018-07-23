from django.conf.urls import url

from GenApp.Sucursal import views

urlpatterns = [
    url(r'^listsucursal/$', views.ListSucursal.as_view()),
    url(r'^listsucursal/(?P<pk>[0-9]+)/$', views.ListSucursalDetail.as_view()),

]
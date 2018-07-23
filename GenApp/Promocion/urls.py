from django.conf.urls import url

from GenApp.Promocion import views

urlpatterns = [
    url(r'^listpromocion/$', views.ListPromocion.as_view()),
    url(r'^listsucursalpro/$', views.ListSucursalPro.as_view()),
    url(r'^listmotivopro/$', views.ListMotivoPro.as_view()),
    url(r'^listmotivos/$', views.ListMotivos.as_view()),
    url(r'^listvales/$', views.ListPromocionVale.as_view()),
    url(r'^listdescuentos/$', views.ListPromocionDescuento.as_view()),
    url(r'^listvales/(?P<pk>[0-9]+)/$', views.ListPromocionValesDetail.as_view()),
    url(r'^listdescuentos/(?P<pk>[0-9]+)/$', views.ListPromocionDescuentoDetail.as_view()),
    url(r'^listmotivos/(?P<pk>[0-9]+)/$', views.ListMotivosDetail.as_view()),
    url(r'^listpromocionquees/$', views.ListPromocionQueEs.as_view()),

]

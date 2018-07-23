from django.conf.urls import url

from GenApp.Producto import views

urlpatterns = [
    url(r'^listproducto/$', views.ListProducto.as_view()),

]

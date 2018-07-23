from django.conf.urls import url

from GenApp.Categoria import views

urlpatterns = [
    url(r'^listcategoria/$', views.ListCategoria.as_view()),
    url(r'^listcategoria/(?P<pk>[0-9]+)/$', views.ListCategoriaDetail.as_view()),

]

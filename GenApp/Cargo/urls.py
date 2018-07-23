from django.conf.urls import url

from GenApp.Cargo import views

urlpatterns = [
    url(r'^listcargo/$', views.ListCargo.as_view()),
    url(r'^listcargo/(?P<pk>[0-9]+)/$', views.ListCargoDetail.as_view()),

]
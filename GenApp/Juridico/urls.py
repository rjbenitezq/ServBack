from django.conf.urls import url

from GenApp.Juridico import views

urlpatterns = [
    url(r'^listjuridico/$', views.ListJuridico.as_view()),

]
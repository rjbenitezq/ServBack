from django.conf.urls import url

from GenApp.Persona import views

urlpatterns = [
    url(r'^listpersona/$', views.ListPersona.as_view()),
    url(r'^listpersona/(?P<pk>[0-9]+)/$', views.ListPersonaDetail.as_view()),

]
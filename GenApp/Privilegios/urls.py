from django.conf.urls import url

from GenApp.Privilegios import views

urlpatterns = [
    url(r'^listOpcion/$', views.OpcionesList.as_view()),

]
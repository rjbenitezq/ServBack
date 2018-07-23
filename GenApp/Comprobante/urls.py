from django.conf.urls import url

from GenApp.Comprobante import views

urlpatterns = [
    url(r'^listcomprobante/$', views.ListComprobante.as_view()),

]
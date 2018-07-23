from django.conf.urls import url

from GenApp.Area import views

urlpatterns = [
    url(r'^listarea/$', views.ListArea.as_view()),
    url(r'^listarea/(?P<pk>[0-9]+)/$', views.ListAreaDetail.as_view()),

]

from django.conf.urls import url
import views;

urlpatterns = [
    url(r'^program$',views.getAll),
    url(r'^$',views.index),
    url(r'^program/(?P<pk>\d+)',views.getelement),
    url(r'^program/count$',views.rowCount),
]

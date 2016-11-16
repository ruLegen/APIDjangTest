
from django.conf.urls import url,include
from django.contrib import admin
import APItest
urlpatterns = [
    url('',include('APItest.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include('APItest.urls'))

]

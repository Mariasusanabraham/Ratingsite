from django.conf.urls import url
from django.contrib import admin
from .import views
from django.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Ratingapp/', include('Ratingapp.urls')),
    url(r'^$', views.hi),
]

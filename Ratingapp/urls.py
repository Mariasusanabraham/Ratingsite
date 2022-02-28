from django.conf.urls import url
from .import views
urlpatterns = [
    
    url(r'^admin', ),
    url(r'^$', views.home),
    url(r'^login', views.login),
    url(r'^save', views.save),
    url(r'^ store', views.store),
    url(r'^logout', views.logout),
    url(r'^details/(?P<id>\d+)', views.details),
    url(r'^description/(?P<id>\d+)', views.description),
    url(r'^review/(?P<id>\d+)/(?P<user_id>\d+)/(?P<Category_id>\d+)', views.review)
    
]
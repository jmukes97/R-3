from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^donate/', views.donate, name='donate'),
    url(r'^donate-objects/', views.donateNM, name='donatestuff'),
    url(r'^request/', views.request, name='request'),


]



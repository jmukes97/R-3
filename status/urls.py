from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^blog/', views.post_list, name='blog'),
    url(r'^home/', views.post_new, name='home'),
]


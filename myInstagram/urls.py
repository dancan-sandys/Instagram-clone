from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^search/$', views.search,  name ='search'),
    url(r'' , views.photos, name='photos'),

]

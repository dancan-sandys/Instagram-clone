from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^search/$', views.search,  name ='search'),
    url(r'^profile/(\d+)$', views.profile, name='profile'),
    url(r'^new/$', views.addphotos, name='addphotos'),
    url(r'^update/$', views.profileupdate, name='profileupdate'),
    url(r'^comment/$', views.new_comment, name='comment'),
    url(r'^like/(\d+)$', views.like, name='like'),
    url(r'^$', views.photos, name='photos'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
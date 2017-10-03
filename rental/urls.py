from django.conf.urls import url
from django.conf.urls import include, url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^api/rental/$',include("rental.api.urls", namespace='rental-api')),
    # url(r'^machine/(?P<machine>[-\w|\W\ ]+)$', views.bymachine, name='machine'),
    # url(r'^company/(?P<company>[-\w|\W\ ]+)$', views.bycompany, name='company'),
    # url(r'^rental/(?P<rental>[-\w|\W\ ]+)$', views.byrental, name='rental'),
    # url(r'^reject$', views.CotainerReject, name='reject'),
]

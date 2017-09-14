from django.conf.urls import url
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^machine/(?P<machine>[-\w|\W\ ]+)$', views.bymachine, name='machine'),
    url(r'^company/(?P<company>[-\w|\W\ ]+)$', views.bycompany, name='company'),
    # url(r'^reject$', views.CotainerReject, name='reject'),
]

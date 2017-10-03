from django.conf.urls import url
from django.contrib import admin

from .views import (
    RentalListAPIView,
    RentalDetailAPIView,
    # RentalCreateAPIView,
    RentalDeleteAPIView
    )

urlpatterns = [
	url(r'^$', RentalListAPIView.as_view(), name='list'),
	# url(r'^create/$', RentalCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>.+)/$', RentalDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<slug>[\w-]+)/delete/$', RentalDeleteAPIView.as_view(),name='delete'),
 
]
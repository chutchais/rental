"""equipmentrental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from django.views.generic.base import TemplateView
from angular.views import AngularTemplateView

urlpatterns = [
	# url(r'^', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^report/', include('rental.urls')),
    url(r'^api/rental/$',include("rental.api.urls", namespace='rental-api')),
    url(r'^api/templates/(?P<item>[A-Za-z0-9\_\-\.\/]+)\.html$',  AngularTemplateView.as_view()),
]

urlpatterns +=  [
    url(r'^', TemplateView.as_view(template_name='angular/home.html'))
]

admin.site.site_header = 'Equipment Rental System'
admin.site.site_title = 'Equipment Rental System'
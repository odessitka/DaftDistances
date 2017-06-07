"""DaftDistances URL Configuration

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
from django.conf.urls import include, url

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from adminplus.sites import AdminSitePlus

from mysite import views

admin.site = AdminSitePlus()
admin.sites.site = admin.site
admin.autodiscover()

urlpatterns = [
    url(r'^distances/', include('distances.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
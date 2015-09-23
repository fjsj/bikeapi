from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('bikes.endpoints_urls')),
    url(r'^', include('bikes.urls')),
)

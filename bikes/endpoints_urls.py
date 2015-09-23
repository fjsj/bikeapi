from django.conf.urls import patterns, include, url

from bikes.endpoints import FileUploadView


urlpatterns = patterns('',
    url(r'^upload/$', FileUploadView.as_view()),
)

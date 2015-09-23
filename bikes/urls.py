from django.conf.urls import patterns, include, url

from bikes.views import SampleView


urlpatterns = patterns('',
    url(r'^$', SampleView.as_view()),
)

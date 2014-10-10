from django.conf.urls import patterns, url

from gcontacts import views

urlpatterns = patterns('',
    url(r'^authorize/$', views.check_google, name='check_google'),
 )
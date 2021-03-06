from django.conf.urls import patterns, url

from pg import views

urlpatterns = patterns('',
    url(r'^contacts/$', views.list_contacts, name='list_contacts'),
    url(r'^contact/745(?P<contact_id>\d+)/$', views.view_contact, name='view_contact'),
    url(r'^contacts/add/$', views.add_contacts, name='add_contacts'),
    url(r'^edit/745(?P<contact_id>\d+)/$', views.edit_contact, name='edit_contact'),
 )

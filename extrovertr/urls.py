from django.conf.urls import patterns, include, url
from django.contrib import admin
from pg.views import create_user_profile

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'extrovertr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('pg.urls')), 
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'home_page.html'}, name='home'),
    url(r'^accounts/login/', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^signup/$', 'pg.views.create_user_profile', name='signup'),
    url(r'^import/', include('gcontacts.urls')),
)

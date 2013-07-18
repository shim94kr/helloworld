from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'polls.views.index'),
    # url(r'^helloworld/', include('helloworld.foo.urls')),
    # url(r'^polls/', 'polls.views.polls', name='polls'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^(?P<poll_id>\d+)/$','polls.views.detail'),
    url(r'^(?P<poll_id>\d+)/vote/$','polls.views.vote'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

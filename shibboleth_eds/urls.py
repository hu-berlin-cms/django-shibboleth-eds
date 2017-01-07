from django.conf.urls import patterns, url

from views import discovery, config

urlpatterns = patterns('',
    url(r'^$', discovery, name='ds'),
    url(r'^idpselect_config.js$', config, name='config'),
)

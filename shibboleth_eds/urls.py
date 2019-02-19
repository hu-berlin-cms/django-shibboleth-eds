from django.conf.urls import url

from views import discovery, config

urlpatterns = [
    url(r'^$', discovery, name='ds'),
    url(r'^idpselect_config.js$', config, name='config'),
]

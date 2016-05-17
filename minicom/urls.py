from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import api
import admin

urlpatterns = patterns('',
    url(r'^api/ping$', api.ping),
    url(r'^api/read$', api.mark_as_read),
    url(r'^api/send$', api.send_message),
	url(r'^api/send_admin$', api.send_message_to_admin),
    url(r'^api/last$', api.n_last_messages),
    url(r'^admin$', admin.users)
)

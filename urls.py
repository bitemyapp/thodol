from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'logout/$', 'django.contrib.auth.views.logout'),
    (r'passchange/$', 'django.contrib.auth.views.password_change', {'post_change_redirect': '/passdone/'}),
    (r'passdone/$', 'django.contrib.auth.views.password_change_done'),
    (r'^', include('thodol.wiki.urls')),
)

import settings
if settings.DEBUG:
    urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),)
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('thodol.wiki.urls')),
)

import settings
if settings.DEBUG:
    urlpatterns += patterns('',(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),)
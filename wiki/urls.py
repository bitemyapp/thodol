from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'thodol.wiki.views.index'),
)

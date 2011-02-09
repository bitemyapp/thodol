from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'thodol.wiki.views.index'),
    (r'^(?P<slug>[-\w]+)/$', 'thodol.wiki.views.page_view'),
    (r'^(?P<slug>[-\w]+)/edit/$', 'thodol.wiki.views.page_edit'),
)

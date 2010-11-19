from django.conf.urls.defaults import *

from modernizr import test_views

urlpatterns = patterns('',
    url(r'^$', test_views.test_view),
    url(r'^content-length/$', test_views.test_view_with_content_length),
    url(r'^charset/$', test_views.test_view_with_charset),
    url(r'^404/$', test_views.test_view_404),
    url(r'^css/$', test_views.test_css),
    url(r'^tag/$', test_views.test_tag),
    url(r'^no-tag/$', test_views.test_no_tag),
)

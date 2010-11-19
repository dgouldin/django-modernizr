"""
Django Modernizr middleware

Some parts borrowed from:
Django Debug Toolbar
Copyright (c) Rob Hudson and individual contributors.
https://github.com/robhudson/django-debug-toolbar
"""
from django.conf import settings
from django.http import HttpResponse, QueryDict
from django.template.loader import render_to_string
from django.utils.encoding import smart_unicode
from django.utils.http import cookie_date

from modernizr.settings import contribute_to_settings

# Default settings needed by ModernizrMiddleware
contribute_to_settings({
    'MODERNIZR_STORAGE': 'cookie',
    'MODERNIZR_COOKIE_NAME': 'modernizr',
    'MODERNIZR_COOKIE_AGE': 60 * 60 * 24 * 7 * 2, # 2 weeks
    'MODERNIZR_COOKIE_DOMAIN': None,
    'MODERNIZR_COOKIE_SECURE': False,
    'MODERNIZR_COOKIE_PATH': '/',
    'MODERNIZR_SESSION_KEY': 'modernizr',
    'MODERNIZR_JS_URL': 'http://cachedcommons.org/cache/modernizr/1.5.0/javascripts/modernizr-min.js',
    'MODERNIZR_SENTINEL_IMAGE_URL': '/django-modernizr-endpoint.gif',
    'MODERNIZR_INCLUDE_TAG': 'body',
})

_HTML_TYPES = ('text/html', 'application/xhtml+xml')

def replace_insensitive(string, target, replacement):
    """
    Similar to string.replace() but is case insensitive
    Code borrowed from: http://forums.devshed.com/python-programming-11/case-insensitive-string-replace-490921.html
    """
    no_case = string.lower()
    index = no_case.rfind(target.lower())
    if index >= 0:
        return string[:index] + replacement + string[index + len(target):]
    else: # no results so return the original string
        return string

class ModernizrMiddleware(object):

    def persist_modernizr(self, request, response):
        data = request.GET
        if settings.MODERNIZR_STORAGE == 'cookie':
            response.set_cookie(settings.MODERNIZR_COOKIE_NAME,
                data.urlencode(),
                max_age=settings.MODERNIZR_COOKIE_AGE,
                expires=cookie_date(settings.MODERNIZR_COOKIE_AGE),
                domain=settings.MODERNIZR_COOKIE_DOMAIN,
                path=settings.MODERNIZR_COOKIE_PATH,
                secure=settings.MODERNIZR_COOKIE_DOMAIN or None)
        elif settings.MODERNIZR_STORAGE == 'session':
            request.session[settings.MODERNIZR_SESSION_KEY] = data
        else:
            raise ValueError("Invalid value for settings.MODERNIZR_STORAGE")
        return response

    def load_modernizr_from_storage(self, request):
        data = None
        if settings.MODERNIZR_STORAGE == 'cookie':
            if settings.MODERNIZR_COOKIE_NAME in request.COOKIES:
                data = QueryDict(request.COOKIES[settings.MODERNIZR_COOKIE_NAME])
        elif settings.MODERNIZR_STORAGE == 'session':
            data = request.session.get(settings.MODERNIZR_SESSION_KEY)

        if data is not None:
            request.modernizr = dict([(k, bool(int(v))) for k,v in data.items()])
        else:
            request.modernizr = None

    def add_modernizr(self, response):
        modernizr_content = render_to_string('modernizr/add_modernizr.html', {
            'modernizr_js_url': settings.MODERNIZR_JS_URL,
            'modernizr_sentinel_img_url': settings.MODERNIZR_SENTINEL_IMAGE_URL,
        })
        tag = u'</' + settings.MODERNIZR_INCLUDE_TAG + u'>'
        response.content = replace_insensitive(
            smart_unicode(response.content), 
            tag,
            smart_unicode(modernizr_content + tag))
        if response.get('Content-Length', None):
            response['Content-Length'] = len(response.content)
        return response

    def process_request(self, request):
        self.load_modernizr_from_storage(request)
        if request.path == settings.MODERNIZR_SENTINEL_IMAGE_URL:
            response = HttpResponse('')
            response = self.persist_modernizr(request, response)
            return response
        else:
            return None

    def process_response(self, request, response):
        if request.modernizr is None and response.status_code == 200 and \
            response['Content-Type'].split(';')[0] in _HTML_TYPES:

            response = self.add_modernizr(response)

        return response
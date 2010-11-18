from django.conf import settings

def contribute_to_settings(defaults):
    for attr, value in defaults.items():
        if not hasattr(settings, attr):
            setattr(settings, attr, value)

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

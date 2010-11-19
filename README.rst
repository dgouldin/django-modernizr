================
Django Modernizr
================

`Modernizr <http://modernizr.com/>`_ is a javascript utility that interrogates
a user's web browser to determine its capabilities.  Unfortunately, all this
delicious data is only available client-side.

django-modernizr is a Django Middleware that includes the Modernizr javascript
and stuffs Modernizr's output into a cookie or session on the first
page request.


Installation
============

#. Add the `modernizr` directory to your Python path.

#. Add the following middleware to your project's `settings.py` file:

   ``'modernizr.middleware.ModenizrMiddleware',``

   The order of MIDDLEWARE_CLASSES is important: the Modernizr Middleware middleware
   must come after any other middleware that encodes the response's content
   (such as GZipMiddleware).

   Note: The modernizr code will only display itself if the mimetype of the
   response is either `text/html` or `application/xhtml+xml` and contains a
   closing `</body>` tag.

   Note: Be aware of middleware ordering and other middleware that may
   intercept requests and return responses.  Putting the modernizr
   middleware *after* the Flatpage middleware, for example, means the
   toolbar will not show up on flatpages.

#. Add `modernizr` to your `INSTALLED_APPS` setting so Django can find the
   template files associated with the modernizr.

   Alternatively, add the path to the modernizr templates
   (``'path/to/modernizr/templates'`` to your ``TEMPLATE_DIRS`` setting.)

Configuration
=============

Django Modernizr has a few settings that can be set in `settings.py`
(all are optional):

#. `MODERNIZR_STORAGE`: set to 'cookie' or 'session'

#. Cookie settings (parity to ``django.contrib.sessions`` cookie settings):

   * `MODERNIZR_COOKIE_NAME`: Name of the cookie. Default is 'modernizr'.
   * `MODERNIZR_COOKIE_AGE`: Expire time of the cookie. Default is 2 weeks.
   * `MODERNIZR_COOKIE_DOMAIN`: Domain name the cookie is issued on.
     Default is None.
   * `MODERNIZR_COOKIE_SECURE`: Whether or not to serve the cookie securely.
     Default is False.
   * `MODERNIZR_COOKIE_PATH`: Path the cookie is issued on. Default is '/'.

#. Session settings:

   * `MODERNIZR_SESSION_KEY`: Session key to use for storage. Default is
     'modernizr'.

#. Modernizr rendering options:

   * `MODERNIZR_JS_URL`: URL to modernizr.js.
     Default is http://cachedcommons.org/cache/modernizr/1.5.0/javascripts/modernizr-min.js .
   * `MODERNIZR_SENTINEL_IMAGE_URL`: URL of sentinel image which includes
     Modernizr data. Default is '/django-modernizr-endpoint.gif'.
   * `MODERNIZR_INCLUDE_TAG`: A closing tag of this type will be located, and
     the Modernizr template will be rendered and inserted just before it.
     Default is 'body'.

Thanks
======

Django Modernizr is a port of Marshall Yount's `rack-modernizr
<https://github.com/marshally/rack-modernizr/>`_.

Portions of code and documentation style were taken from Rob Hudson's
`django-debug-toolbar
<https://github.com/robhudson/django-debug-toolbar>`_.

from django.conf import settings
from django.http import HttpResponse
from django.test import TestCase

class ModernizrMiddlewareTest(TestCase):
    urls = 'modernizr.test_urls'

    def test_no_cookie(self):
        """
        Tests response when modernizr cookie has not been set.
        """
        response = self.client.get('/')
        self.assertContains(response, 'script')

    def test_cookie(self):
        """
        Tests response when modernizr cookie has been set.
        """
        url = '%s?a=b&c=d&e=f' % settings.MODERNIZR_SENTINEL_IMAGE_URL
        response = self.client.get(url)
        self.assertTrue(settings.MODERNIZR_COOKIE_NAME in response.cookies)

    def test_correct_content_length(self):
        """
        Tests that ModernizrMiddleware successfully changes the
        response content-length header.
        """
        response = self.client.get('/content-length/')
        original_length = len("<html><body>Hello World</body></html>")
        self.assertNotEqual(response['Content-Length'], original_length)

    def test_charset(self):
        """
        Tests the addition of a charset parameter to Content-Type header.
        """
        response = self.client.get('/charset/')
        self.assertContains(response, 'script')

    def test_modernizr_js_url(self):
        """
        Tests assigning to settings.MODERNIZR_JS_URL.
        """
        settings.MODERNIZR_JS_URL = 'http://distinctive.domain.com/modernizr.js'

        response = self.client.get('/')
        self.assertContains(response, settings.MODERNIZR_JS_URL)

    def test_cookie_name(self):
        """
        Tests assigning to settings.MODERNIZR_COOKIE_NAME.
        """
        settings.MODERNIZR_COOKIE_NAME = 'distinctive_name'

        url = '%s?a=b&c=d&e=f' % settings.MODERNIZR_SENTINEL_IMAGE_URL
        response = self.client.get(url)
        self.assertTrue(settings.MODERNIZR_COOKIE_NAME in response.cookies)

    def test_non_200(self):
        """
        Tests for response codes other than 200.
        """
        response = self.client.get('/404/')
        self.assertNotContains(response, 'script', status_code=404)

    def test_non_html_response(self):
        """
        Tests for response type other than those supported.
        """
        response = self.client.get('/css/')
        self.assertNotContains(response, 'script')

    def test_tag(self):
        """
        Tests assigning to settings.MODERNIZR_INCLUDE_TAG.
        """
        settings.MODERNIZR_INCLUDE_TAG = 'head'

        response = self.client.get('/tag/')
        self.assertContains(response, '</script>\n</head>')

    def test_no_tag(self):
        """
        Tests the absence of the correct closing tag.
        """
        response = self.client.get('/no-tag/')
        self.assertNotContains(response, 'script')

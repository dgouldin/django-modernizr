from django.http import HttpResponse, HttpResponseNotFound

def test_view(request):
    content = '<html><body>Hello World</body></html>'
    response = HttpResponse(content)
    return response

def test_view_with_content_length(request):
    content = '<html><body>Hello World</body></html>'
    response = HttpResponse(content)
    response['Content-Length'] = len(content)
    return response

def test_view_with_charset(request):
    content = '<html><body>Hello World</body></html>'
    response = HttpResponse(content)
    response['Content-Type'] = 'text/html; charset=utf-8'
    return response

def test_view_404(request):
    content = '<html><body>Hello World</body></html>'
    response = HttpResponseNotFound(content)
    return response

def test_css(request):
    content = 'body { display: none; }'
    response = HttpResponse(content)
    response['Content-Type'] = 'text/css'
    return response

def test_tag(request):
    content = '<html><head></head><body>Hello World</body></html>'
    response = HttpResponse(content)
    return response

def test_no_tag(request):
    content = '<html>Malformed document</html>'
    response = HttpResponse(content)
    return response

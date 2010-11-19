import os.path
import sys

PROJECT_ROOT = os.path.dirname(__file__)
REPO_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, '..'))
sys.path.insert(0, REPO_ROOT)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db',
        'TEST_NAME': 'other_db',
    },
}
SECRET_KEY = '@vjdp36cgfz6xq^^&c9bb&-353uz^j1xy*avt*z@rpotf-i4vv'
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'modernizr.middleware.ModernizrMiddleware',
)
ROOT_URLCONF = 'example_project.urls'
TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
)
INSTALLED_APPS = (
    'django.contrib.sessions',
    'modernizr',
)

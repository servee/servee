import os

BASE_DIR = os.path.dirname(__file__)

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.flatpages",
    "django.contrib.sessions",
    "django.contrib.contenttypes",
    "frontendadmin",
    "servee",
)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.request',
)

ROOT_URLCONF = "frontendadmin.tests.urls"

SITE_ID = 1

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
    }
}

TIME_ZONE = "America/New_York"
LANGUAGE_CODE = "en-us"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = os.path.join(PROJECT_ROOT,"site_media","media")
MEDIA_URL = "/site_media/media/"
STATIC_ROOT = os.path.join(PROJECT_ROOT,"site_media","static")
STATIC_URL = "/site_media/static/"
ADMIN_MEDIA_PREFIX = "/site_media/static/admin/"

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, "static"),
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

SECRET_KEY = "$dqgg1dt%!19ms5j1t4+7fixlqzp7&ji_^vhq7!g$r5#*(@=kf"

TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
]

ROOT_URLCONF = "example_project.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        "django.request":{
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    "django.contrib.admindocs",

    # We're going to assume flatpages is
    # Installed, and that is the app that
    # you want to be editable.
    "django.contrib.flatpages",

    # servee dependancies
    "uni_form",

    # servee
    "servee.frontendadmin",
    "servee.wysiwyg",

    # tinymce is currently the only
    # supported wysiwyg backend.
    # I'd like to support a "none (plain html)" backend
    # and also possibly a markdown backend.
    # There are other cool editors poping up as well,
    # Aloha, Dojo, and classics like FCK.  Please contribute.
    "servee_redactor",

    # sample insert, a nieve image placer.
    "sample_image_insert",

    # minimal app that is used to write servee forms/registrations
    # for the flatpages app.  This is the convention for adding servee
    # frontend editing to 3rd party apps.
    "servee_extensions",
]

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"

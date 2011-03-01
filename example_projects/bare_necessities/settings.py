# Django settings for bare_necessities project.
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

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    'django.middleware.csrf.CsrfResponseMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",


    "servee.wysiwyg.middleware.WysiwygMiddleware",
    "servee.toolbar.middleware.ToolbarMiddleware",
    
    # Flatpage Fallback middleware must go AFTER servee
    # Middleware if you are using it.
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",    

)

ROOT_URLCONF = "bare_necessities.urls"

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
)

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
    "frontendadmin",
    "easy_thumbnails",
    "uni_form",
    "improved_inlines",

    # servee
    "servee",
    "servee.wysiwyg",
    "servee.wysiwyg.tinymce",
    "servee.toolbar",

    # media
    "servee.contrib.media.image",
    "servee.contrib.media.video",
    "servee.contrib.media.document",
    "servee.contrib.media.gallery",

    # toolbars
    "servee.contrib.tools.gallery",
]
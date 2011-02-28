The docs aren't built, this is an alpha version of servee and may contain many bugs.

The development version of Servee requires Django 1.3 or later.

First you should put servee in your environment:

    pip install -e git+git://github.com/servee/servee.git#egg=django-servee
    # servee is on PyPI as django-servee, but it is out of date

or download and

    ./setup.py install

or if you want to hack on the code, create a symlink in your site-packages
    
    ./setup.py develop

If pip is not setup to read the other dependancies from there so navigate to your servee folder in your path now (<env>/src/servee, or wherever you downloaded from) and do pip install -r requirements.txt

Then add servee to installed apps and add the two middleware packages.

    INSTALLED_APPS = [
        #servee_dependancies
        "frontendadmin",
        "staticfiles",
        "easy_thumbnails",
        "uni_form",
    
        #servee
        "servee",
        "improved_inlines",
        "servee.wysiwyg",
        "servee.wysiwyg.tinymce",
        "servee.toolbar",

        #media
        "servee.contrib.media.image",
        "servee.contrib.media.video",
        "servee.contrib.media.document",
        "servee.contrib.media.gallery",

        #toolbars
        "servee.contrib.tools.gallery",    
    ]

MIDDLEWARE_CLASSES
    
    "servee.wysiwyg.middleware.WysiwygMiddleware",
    "servee.toolbar.middleware.ToolbarMiddleware",

Also Add this setting to settings.py

    # Currently, it's overkill, since there is just one WYSIWYG
    # Editor supported.
    SRV_WYSIWYG_EDITOR = "tinymce"

Then syncdb and collectstatic (if you are on production)

It's important to add servee urls and frontendadmin urls

    url(r"^servee/", include("servee.urls")),
    url(r"^fa/", include("frontendadmin.urls")),
    

Add to your base template

    <link rel="stylesheet" href="{{ STATIC_URL }}css/djAdmin.css" />

Now change your templates on pages you wish to edit to add [frontend admin][fa]:


[fa][http://github.com/bartTC/django-frontendadmin]

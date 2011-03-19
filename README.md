* On Freenode #servee
* Docs at [[http://django-servee.readthedocs.org/en/latest/index.html|Read The Docs]]


This is an alpha version of servee and may contain many bugs.

First you should put servee in your environment:

    pip install -e git+git://github.com/servee/servee.git@features/replace_frontendadmin#egg=django-servee
    # servee is on PyPI as django-servee, but it is out of date

or download and

    ./setup.py develop

I pip is not setup to read the other dependancies from there so navigate to your servee folder in your path now (<env>/src/servee, or wherever you downloaded from) and do pip install -r requirements.txt

Then add servee to installed apps and add the two middleware packages.

    INSTALLED_APPS = [
        #servee_dependancies
        "uni_form",
    
        #servee
        "servee",
        "improved_inlines",
        "servee.wysiwyg",
        "servee.wysiwyg.tinymce",

        #media
        "servee.contrib.media.image",    
    ]

Also Add this setting to settings.py

    # Currently, it's overkill, since there is just one WYSIWYG
    # Editor supported. Please write and submit another :)
    SRV_WYSIWYG_EDITOR = "tinymce"

Then syncdb, or migrate and collectstatic (if you are on production)

It's important to add servee urls and frontendadmin urls
    
    from servee import frontendadmin
    url(r"^servee/", include(frontendadmin.site.urls)),

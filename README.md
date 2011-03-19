* On Freenode #servee
* Docs at [[http://django-servee.readthedocs.org/en/latest/index.html|Read The Docs]]


This is an alpha version of servee and may contain many bugs.

First you should put servee in your environment:

    pip install -e git+git://github.com/servee/servee.git@features/replace_frontendadmin#egg=django-servee
    # servee is on PyPI as django-servee, but it is out of date if you're looking for the
    # development version

or download and

    ./setup.py develop

Then add servee to installed apps and add the two middleware packages.

    INSTALLED_APPS = [
        #servee_dependancies
        "uni_form",
    
        #servee
        "servee.frontendadmin",
        "servee.wysiwyg",
        "servee.wysiwyg.tinymce", 
    ]

Then syncdb, or migrate and collectstatic (if you are on production)

It's important to add servee urls and frontendadmin urls
    
    from servee import frontendadmin
    url(r"^servee/", include(frontendadmin.site.urls)),

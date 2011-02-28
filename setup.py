from setuptools import setup, find_packages

setup(
    name='django-servee',
    version=__import__('servee').__version__,
    description=__import__('servee').__about__,
    long_description=open('README.md').read(),
    # Get more strings from http://www.python.org/pypi?:action=list_classifiers
    author='Kelly Creative Tech - Issac Kelly',
    author_email='issac@kellycreativetech.com',
    url='http://www.servee.com',
    #download_url='http://github.com/robhudson/django-debug-toolbar/downloads',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    
    dependency_links = [
           "http://www.djangoproject.com/download/1.3-beta-1/tarball/#egg=django-1.3-beta-1"
       ],
    
    install_requires=['django>=1.3-beta-1', 'django-frontendadmin>=0.4', 'django-staticfiles>=1.0b1',
                'easy-thumbnails>=1.0-alpha-15', 'django-uni-form>=0.7.0', 'django-improved-inlines>=0.2',
                'beautifulsoup>=3.2.0',
                ],
)

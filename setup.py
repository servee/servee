from setuptools import setup, find_packages

setup(
    name='django-servee',
    version=__import__('servee').__version__,
    description=__import__('servee').__about__,
    long_description=open('README.rst').read(),
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
)

#!/usr/bin/env python

import os, sys

os.environ["DJANGO_SETTINGS_MODULE"] = "test_settings"

parent = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
sys.path.insert(0, parent)
sys.path.insert(0, root)

from django.test.simple import DjangoTestSuiteRunner
from django.conf import settings

def runtests():
    runner = DjangoTestSuiteRunner()
    failures = runner.run_tests(["frontendadmin"], verbosity=1, interactive=True)
    sys.exit(failures)

if __name__ == "__main__":
    runtests()


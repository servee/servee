from unittest import TestCase as UnittestTestCase
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
from django.template import RequestContext, Template
from django.test import Client, TestCase

# Django 1.3's RequestFactory doesn't run requests through MiddleWare
from helpers import RequestFactory


class SpaceOutTestCase(UnittestTestCase):
    def test_variants(self):
        from servee.utils import space_out_camel_case

        self.assertEqual(space_out_camel_case('nospacesanywhere'), 'nospacesanywhere')
        self.assertEqual(space_out_camel_case('A'), 'A')
        self.assertEqual(space_out_camel_case('AB'), 'AB')
        self.assertEqual(space_out_camel_case('Abc'), 'Abc')
        self.assertEqual(space_out_camel_case('ABc'), 'A Bc')
        self.assertEqual(space_out_camel_case('AbCd'), 'Ab Cd')
        self.assertEqual(space_out_camel_case('TypicalCamelCase'), 'Typical Camel Case')
        self.assertEqual(space_out_camel_case('DMLSServicesOtherBSTextLLC'), 'DMLS Services Other BS Text LLC')


class TestTemplateTags(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="test")
        self.user.set_password("secret")
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()

        self.factory = RequestFactory()

        FlatPage.objects.create(
            url="/",
            title="Test",
            content="This is a test.",
        )

    def tearDown(self):
        pass

    def get_request_for_url(self, url):
        request = self.factory.get(url)
        user = authenticate(username=self.user.username, password="secret")
        login(request, user)
        return request

    def test_frontendadmin_add(self):
        frontendadmin_add_html = """<a class="frontendadmin frontendadmin_add" href="/servee/flatpages/flatpage/add/">Add a Flatpage</a>"""
        frontendadmin_add_plain_html = """<a class="frontendadmin frontendadmin_add" href="/servee/flatpages/flatpage/add/">Add</a>"""
        template = Template("""\
{% load frontendadmin_tags %}\
{% frontendadmin_add flatpages "Add a Flatpage" %}\
"""     )
        template_plain = Template("""\
{% load frontendadmin_tags %}\
{% frontendadmin_add flatpages %}\
"""     )
        request = self.get_request_for_url("/frontendadmin_add/")

        flatpages = FlatPage.objects.all()
        context = RequestContext(request, {"flatpages": flatpages})
        # Test with custom label
        content = template.render(context)
        self.assertEqual(content, frontendadmin_add_html)
        # Test without custom label
        content = template_plain.render(context)
        self.assertEqual(content, frontendadmin_add_plain_html)

    def test_frontendadmin_change(self):
        frontendadmin_change_html = """<a class="frontendadmin frontendadmin_edit" href="/servee/flatpages/flatpage/1/">Edit This Flatpage</a>"""
        frontendadmin_change_plain_html = """<a class="frontendadmin frontendadmin_edit" href="/servee/flatpages/flatpage/1/">Change</a>"""
        template = Template("""\
{% load frontendadmin_tags %}\
{% frontendadmin_change flatpage "Edit This Flatpage" %}\
"""     )
        template_plain = Template("""\
{% load frontendadmin_tags %}\
{% frontendadmin_change flatpage %}\
"""     )
        request = self.get_request_for_url("/frontendadmin_change/")

        flatpage = FlatPage.objects.get(pk=1)
        context = RequestContext(request, {"flatpage": flatpage})
        # Test with custom label
        content = template.render(context)
        self.assertEqual(content, frontendadmin_change_html)
        # Test without custom label
        content = template_plain.render(context)
        self.assertEqual(content, frontendadmin_change_plain_html)

    def test_frontendadmin_delete(self):
        frontendadmin_delete_html = """<a class="frontendadmin frontendadmin_delete" href="/servee/flatpages/flatpage/1/delete/">Delete This Flatpage</a>"""
        frontendadmin_delete_plain_html = """<a class="frontendadmin frontendadmin_delete" href="/servee/flatpages/flatpage/1/delete/">Delete</a>"""
        template = Template("""\
{% load frontendadmin_tags %}\
{% frontendadmin_delete flatpage "Delete This Flatpage" %}\
"""     )
        template_plain = Template("""\
{% load frontendadmin_tags %}\
{% frontendadmin_delete flatpage %}\
"""     )
        request = self.get_request_for_url("/frontendadmin_delete/")

        flatpage = FlatPage.objects.get(pk=1)
        context = RequestContext(request, {"flatpage": flatpage})
        # Test with custom label
        content = template.render(context)
        self.assertEqual(content, frontendadmin_delete_html)
        # Test without custom label
        content = template_plain.render(context)
        self.assertEqual(content, frontendadmin_delete_plain_html)

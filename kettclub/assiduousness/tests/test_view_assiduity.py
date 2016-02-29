from django.test import TestCase
from django.shortcuts import resolve_url as r
from kettclub.assiduousness.forms import AssiduityForm


class SubscriptionsNewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('assiduousness:new'))

    def test_get(self):
        """Get /inscrição/ must return code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use sbscription/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'assiduousness/assiduity_form.html')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, AssiduityForm)

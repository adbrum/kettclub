from django.test import TestCase
from django.shortcuts import resolve_url as r
from kettclub.monthlyplans.forms import MonthlyPlansForm


class SubscriptionsNewGet(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('monthlyplans:new'))

    def test_get(self):
        """Get /inscrição/ must return code 200 """
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use monthlyplans/add.html"""
        self.assertTemplateUsed(self.resp, 'monthlyplans/add.html')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, MonthlyPlansForm)


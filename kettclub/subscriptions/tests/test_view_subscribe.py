from django.test import TestCase
from django.shortcuts import resolve_url as r
from kettclub.core.models import Atleta
from kettclub.subscriptions.forms import SubscriptionForm


class SubscriptionsNewGet(TestCase):
    def setUp(self):
        self.response = self.client.get(r('subscriptions:new'))

    def test_get(self):
        """Get /inscricao/ must return code 200 """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use sbscription/subscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/add.html')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_html_content(self):
        """HTML must contain input tags"""
        contents = ['<form method="post"', '<div class="panel-body"']

        for content in contents:
            with self.subTest():
                self.assertContains(self.response, content)

        contents = [
            (1, '<form method="post"'),
            (1, '<div class="panel-body"'),
        ]

        for count, content in contents:
            with self.subTest():
                self.assertContains(self.response, content, count)

    def test_csrf(self):
        """ HTML must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class SubscriptionsNewPostValid(TestCase):
    def setUp(self):
        self.data = dict(planomensalidade=1, nome='Lisandra', sobrenome='Ferreira', emailatleta='teste@teste.com',
                         datainicio='23/06/2016',
                         datanascimento='23/06/2016', idade=42, cc=123456, nif=123456, telefone='966085448',
                         telefone2='966085448',
                         ativo=True)

    def test_post(self):
        """Valid POST should redirect to /inscricao/1/"""
        self.response = self.client.post(r('subscriptions:new'), self.data)


class SubscriptionsNewPostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post(r('subscriptions:new'), {})

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(302, self.response.status_code)

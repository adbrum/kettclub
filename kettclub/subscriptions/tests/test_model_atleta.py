from datetime import datetime

from django.test import TestCase
from kettclub.core.models import Atleta


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Atleta(
            planomensalidade_id=1,
            nome='Zé',
            sobrenome=' Ruela',
            emailatleta='ruela@gmail.com',
            datainicio='2016-01-20',
            datanascimento='2016-01-20',
            idade='42',
            cc='123456',
            nif='123456',
            telefone='9660608545',
            telefone2='9660608545',
            ativo=True
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(Atleta.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Zé', str(self.obj.nome))

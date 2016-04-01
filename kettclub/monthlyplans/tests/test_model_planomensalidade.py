from datetime import datetime

from django.test import TestCase
from kettclub.core.models import PlanoMensalidade


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = PlanoMensalidade(
            nome='KC Rapidinha',
            valor=15.00,
            horario='Tarde',
            ativo=True
        )

        self.obj.save()

    def test_create(self):
        self.assertTrue(PlanoMensalidade.objects.exists())

    def test_created_at(self):
        """PlanoMensalidade must have an auto created_at attr."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('KC Rapidinha', str(self.obj.nome))

import unittest
from cryptos.serializer import CriptosUserSerializer
from cryptos.models import Criptos
from datetime import date

class MyTestCase(unittest.TestCase):

    def setUp(self):

        self.criptouser_attributes = {
            'id_c': 2,
            'name': 'Platzicoin',
            'purchase_price': 12.3,
            'take_profit': 100.2,
            'stop_loss': 8.2,
            'cantity': 1,
            'able': 0,
            'date_purchase': date.today(),
            'user_fk': 1
        }

        self.criptouser_data = {
            'id_c': 1,
            'name': 'Mexicoin',
            'purchase_price': 11.3,
            'take_profit': 220.2,
            'stop_loss': 5.2,
            'cantity': 2,
            'able': 1,
            'date_purchase': date.today(),
            'user_fk': 3
        }

        self.criptouser = Criptos.objects.create(**self.criptouser_attributes)
        self.serializer = CriptosUserSerializer(instance=self.criptouser)

    def test_contains_expected_fields(self):

        data = self.serializer.data

        self.assertCountEqual(data.keys(), ['id_c',
                                            'name',
                                            'purchase_price',
                                            'take_profit',
                                            'stop_loss',
                                            'cantity',
                                            'able',
                                            'date_purchase',
                                            'user_fk'])


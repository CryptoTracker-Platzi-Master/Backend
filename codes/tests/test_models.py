from django.test import TransactionTestCase


class TaskModelTransactionTestCase(TransactionTestCase):
    fixtures = ['codes/fixtures/unit-tests.json']
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class ProductsListTest(TestCase):
    def setUp(self):
        self.c = APIClient()

    def test_products_list(self):
        response = self.c.get(
            '/products/catalog/products/'
        )
        print(response.status_code)
        print(response.data)
        self.assertEqual(True, True)


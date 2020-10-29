import pytz
from datetime import datetime, timedelta
import json
from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.test import APIClient
from products.models import Catalog, Product
from uuid import uuid4


def _dict_key_quotes(text):
    """ Replaces first two occurrences of double quotes " to single quotes ' in every line
        Is used to print dictionaries formatted according to the project guidelines
        (dict key are in single quotes, texts are in double quotes)
    """
    return '\n'.join([l.replace('"', "'", 2) for l in text.split('\n')])


def dump(response):
    """ Print DRF response data
        Useful for debugging tests. Prints response code and indented JSON data
    :param response: server response provided by DRF testing client (APIClient)
    """

    print("\nURL:", response.request['PATH_INFO'])
    print("Method:", response.request['REQUEST_METHOD'])
    if response.request['QUERY_STRING']:
        print("Query:", response.request['QUERY_STRING'])
    print("\n")
    print("Status code:\n{}\n\nData:\n{}\n".format(
        response.status_code,
        _dict_key_quotes(json.dumps(response.data, indent=4, ensure_ascii=False))
        if hasattr(response, 'data') else None
    ))


class ProductsListTest(TestCase):

    def setUp(self):
        self.c = APIClient()

        user_kw = dict(
            username='tt',
            password='111',
            email='tt' + '.com'
        )

        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.catalog = Catalog.objects.create(slug=str(uuid4()))
        self.product = Product.objects.create(name='aaaaa',price=20.00, stock=10, catalog_id=self.catalog.id)
        self.product1 = Product.objects.create(name='aabbbb', price=10.00, stock=5, catalog_id=self.catalog.id)
        self.product2 = Product.objects.create(name='babb', price=15.00, stock=3, catalog_id=self.catalog.id)

    def test_products_search(self):
        self.c.login(username='tt', password='111')

        response = self.c.get(
            '/products/catalog/products/?search=aaa')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dump(response)

        created_on = self.product.created_on
        updated_on = self.product.updated_on

        tz = pytz.timezone('Europe/Kiev')
        created_on = created_on.replace(tzinfo=pytz.UTC)
        created_on = created_on.astimezone(tz)
        updated_on = updated_on.replace(tzinfo=pytz.UTC)
        updated_on = updated_on.astimezone(tz)

        self.assertEqual(response.data, {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.product.id,
                        "type": "product",
                        "catalog": self.catalog.id,
                        "name": 'aaaaa',
                        "slug": '',
                        "price": '20.00',
                        "stock": self.product.stock,
                        "available": True,
                        "created_on": created_on.isoformat(),
                        "updated_on": updated_on.isoformat(),
                        "created_by": None,
                        "updated_by": None
                    }
                ]
            }
        )
        print(response.data)

        response = self.c.get(
            '/products/catalog/products/?search=aab')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dump(response)

        created_on1 = self.product1.created_on
        updated_on1 = self.product1.updated_on

        tz = pytz.timezone('Europe/Kiev')
        created_on1 = created_on1.replace(tzinfo=pytz.UTC)
        created_on1 = created_on1.astimezone(tz)
        updated_on1 = updated_on1.replace(tzinfo=pytz.UTC)
        updated_on1 = updated_on1.astimezone(tz)

        self.assertEqual(response.data, {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.product1.id,
                        "type": "product",
                        "catalog": self.catalog.id,
                        "name": 'aabbbb',
                        "slug": '',
                        "price": '10.00',
                        "stock": self.product1.stock,
                        "available": True,
                        "created_on": created_on1.isoformat(),
                        "updated_on": updated_on1.isoformat(),
                        "created_by": None,
                        "updated_by": None
                    }
                ]
            }
        )
        print(response.data)

        response = self.c.get(
            '/products/catalog/products/?search=babb')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dump(response)

        created_on2 = self.product2.created_on
        updated_on2 = self.product2.updated_on

        tz = pytz.timezone('Europe/Kiev')
        created_on2 = created_on2.replace(tzinfo=pytz.UTC)
        created_on2 = created_on2.astimezone(tz)
        updated_on2 = updated_on2.replace(tzinfo=pytz.UTC)
        updated_on2 = updated_on2.astimezone(tz)

        self.assertEqual(response.data, {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.product2.id,
                        "type": "product",
                        "catalog": self.catalog.id,
                        "name": 'babb',
                        "slug": '',
                        "price": '15.00',
                        "stock": self.product2.stock,
                        "available": True,
                        "created_on": created_on2.isoformat(),
                        "updated_on": updated_on2.isoformat(),
                        "created_by": None,
                        "updated_by": None
                    }
                ]
            }
        )
        print(response.data)

        response = self.c.get(
            '/products/catalog/products/?search=aa')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dump(response)
        self.assertEqual(response.data, {
                "count": 2,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.product.id,
                        "type": "product",
                        "catalog": self.catalog.id,
                        "name": 'aaaaa',
                        "slug": '',
                        "price": '20.00',
                        "stock": self.product.stock,
                        "available": True,
                        "created_on": created_on.isoformat(),
                        "updated_on": updated_on.isoformat(),
                        "created_by": None,
                        "updated_by": None
                    },
                    {
                        "id": self.product1.id,
                        "type": "product",
                        "catalog": self.catalog.id,
                        "name": 'aabbbb',
                        "slug": '',
                        "price": '10.00',
                        "stock": self.product1.stock,
                        "available": True,
                        "created_on": created_on1.isoformat(),
                        "updated_on": updated_on1.isoformat(),
                        "created_by": None,
                        "updated_by": None
                    },
                ]
            }
        )

        print(response.data)

        response = self.c.get(
            '/products/catalog/products/?search=qqqq')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dump(response)
        self.assertEqual(response.data, {
                'count': 0,
                'next': None,
                'previous': None,
                'results': []
            }
        )
        print(response.data)

    def test_products_create(self):
        self.assertEqual(True, True)


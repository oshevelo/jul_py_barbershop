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
    print("*" * 100)
    print("To run the test, you must disable the IsReadOnly permission")
    print("*" * 100)

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
        self.product = Product.objects.create(name='aaaaa',price=20.00, stock=10, catalog_id=self.catalog.id
        )

    def test_products_edit(self):

        created_on = self.product.created_on
        updated_on = self.product.updated_on
        tz = pytz.timezone('Europe/Kiev')
        created_on = created_on.replace(tzinfo=pytz.UTC)
        created_on = created_on.astimezone(tz)
        updated_on = updated_on.replace(tzinfo=pytz.UTC)
        updated_on = updated_on.astimezone(tz)

        self.c.login(username='tt', password='111')

        response = self.c.post(
            '/products/catalog/products/',
            data=
            {
                "type": "product",
                "catalog": self.catalog.id,
                "name": "000000000000",
                "slug": "000000000000",
                "price": "11.00",
                "stock": 20,
                "available": True
            },
            format='json'
        )
        dump(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # print(_dict_key_quotes(json.dumps({
        #      "id": response.data['id'],
        #      "type": "product",
        #      "catalog": self.catalog.id,
        #      "name": "000000000000",
        #      "slug": "000000000000",
        #      "price": "11.00",
        #      "stock": 20,
        #      "available": True,
        #      "created_on": response.data['created_on'],
        #      "updated_on": response.data['updated_on'],
        #      "created_by": self.user.id,
        #      "updated_by": self.user.id
        #  }, indent=4, ensure_ascii=False)))

        self.assertEqual(response.data,
                         {
                             "id": response.data['id'],
                             "type": "product",
                             "catalog": self.catalog.id,
                             "name": "000000000000",
                             "slug": "000000000000",
                             "price": "11.00",
                             "stock": 20,
                             "available": True,
                             "created_on": response.data['created_on'],
                             "updated_on": response.data['updated_on'],
                             "created_by": self.user.id,
                             "updated_by": self.user.id
                         }
                         )
        print(response.data)
        print('*'*100)



    def test_products_create(self):
        self.assertEqual(True, True)

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
from apps_generic.dump import dump


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
        self.product = Product.objects.create(name='aaaaa',price=20.00, stock=20, catalog_id=self.catalog.id)

    def test_products_delete(self):
        created_on = self.product.created_on
        updated_on = self.product.updated_on

        tz = pytz.timezone('Europe/Kiev')
        created_on = created_on.replace(tzinfo=pytz.UTC)
        created_on = created_on.astimezone(tz)
        updated_on = updated_on.replace(tzinfo=pytz.UTC)
        updated_on = updated_on.astimezone(tz)


        self.c.login(username='tt', password='111')
        response = self.c.delete(
            '/products/catalog/products/{}/'.format(self.product.id)
        )

        dump.dump(response)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(response.data,
                         None
                         )
        print(response.data)













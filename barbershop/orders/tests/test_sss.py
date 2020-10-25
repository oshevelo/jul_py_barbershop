import json
from datetime import datetime
from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from orders.models import Order
from cart.models import Cart


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


class OrdersListAPITest(TestCase):
    def setUp(self):
        self.c = APIClient()
        user_kw = dict(
            username='tt',
            password='111',
            email='tt' + '.com'
        )
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.cart = Cart.objects.create(pub_date=datetime.now(), user=self.user)
        self.order = Order.objects.create(order_sum=10.01, cart=self.cart)

    def test_orders_list(self):
        self.c.login(username='tt', password='111')
        response = self.c.get(
            '/orders/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # dump(response)
        self.assertEqual(response.data, {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "client": None,
                    "cart": {
                        "id": self.cart.id
                    },
                    "order_sum": str(self.order.order_sum),
                    "order_id": self.order.order_id
                }
            ]
        }
                         )

    def test_orders_created(self):
        self.c.login(username='tt', password='111')
        response = self.c.post(
            '/orders/'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # dump(response)
        self.assertEqual(response.data, {
            "client": None,
            "cart": {
                "id": self.cart.id
            },
            "order_sum": str(self.order.order_sum),
            "order_id": self.order.order_id
        }
                         )

    def test_cart_list(self):
        self.c.login(username='tt', password='111')
        response = self.c.get(
            '/cart/'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # dump(response)

    def test_cart_prohibited_list(self):
        # self.c.login(username='tt', password='111')
        response = self.c.get(
            '/cart/'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # dump(response)
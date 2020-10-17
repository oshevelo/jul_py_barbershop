# from datetime import datetime
#
# from django.test import TestCase
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User
#
# from rest_framework import status
# from rest_framework.test import APIClient
#
# from ..orders.models import Order
# from ..cart.models import Cart
#
# class OrdersListAPITest(TestCase):
#
#     def setUp(self):
#         self.c = APIClient()
#         user_kw = dict(
#             username='tt',
#             password='111',
#             email='tt' + '.com'
#         )
#         user_kw['password'] = make_password(user_kw['password'])
#         self.user = User.objects.create(**user_kw)
#         self.cart = Cart.objects.create(pub_date=datetime.now(), user = self.user)
#         self.order = Order.objects.create(order_sum=10.01, cart=self.cart)
#
#
#     def test_orders_list(self):
#
#         self.c.login(username='tt', password='111')
#         response = self.c.get(
#             '/orders/'
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         print(self.order.order_sum)
#         self.assertEqual(response.data, {
#                 "count": 1,
#                 "next": None,
#                 "previous": None,
#                 "results": [
#                     {
#                         "client": None,
#                         "cart": {
#                             "id": self.cart.id
#                         },
#                         "order_sum": str(self.order.order_sum),
#                         "order_id": self.order.order_id
#                     }
#                 ]
#             }
#         )
#
#     def test_orders_create(self):
#         self.assertEqual(True, True)

import json
from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient

from worker_profile.models import WorkerProfile, WorkerCommunications


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


class WorkerProfileCreateAPITest(TestCase):
    def setUp(self):
        self.c = APIClient()
        user_kw = dict(
            username='tt',
            password='111',
            email='tt' + '.com'
        )
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)

    def test_worker_profile_create(self):
        self.c.login(username='tt', password='111')
        response = self.c.post(
            '/worker_profile/worker_profile/',
            data={
                'first_name': ['testtest'],
                'second_name': ['testtesttest'],
                'position': ['admin'],
                'phone_number': ['+222222222222'],
                'email': ['testtesttesttest@gmail.com'],
                'worker': self.user.id,
            }
        )

        dump(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
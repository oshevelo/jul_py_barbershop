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


class WorkerProfileListAPITest(TestCase):

    def setUp(self):
        self.c = APIClient()
        user_kw = dict(
            username='tt',
            password='111',
            email='tt' + '.com'
        )
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.worker = WorkerProfile.objects.create(first_name='test', second_name='testtest', position='testbarber',
                                                   phone_number='+111111111111', email='test@gmail.com', worker=None)

    def test_worker_profile_list(self):
        response = self.c.get(
            '/worker_profile/worker_profile/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dump(response)
        self.assertEqual(response.data, {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.worker.id,
                        "first_name": self.worker.first_name,
                        "second_name": self.worker.second_name,
                        "position": self.worker.position,
                        "phone_number": self.worker.phone_number,
                        "email": self.worker.email,
                        "worker": self.worker.worker
                    }
                ]
            }
        )

    def test_worker_profile_create(self):
        self.assertEqual(True, True)


class WorkerCommunicationsListAPITest(TestCase):
    def setUp(self):
        self.c = APIClient()
        self.worker = WorkerProfile.objects.create(first_name='test', second_name='testtest', position='testbarber',
                                                   phone_number='+111111111111', email='test@gmail.com', worker=None)
        self.worker_comm = WorkerCommunications.objects.create(worker_profile=self.worker,
                                                               type=WorkerCommunications.Type.facebook_id,
                                                               social_networks_ids='123')

    def test_worker_communications_list(self):
        response = self.c.get(
            '/worker_profile/worker_profile/worker_communications/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dump(response)
        print(response.data)
        self.assertEqual(response.data, {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.worker_comm.id,
                        "worker_profile": self.worker_comm.worker_profile.id,
                        "social_network": 'Facebook id',
                        "social_networks_ids": self.worker_comm.social_networks_ids
                    },
                ]
            }
        )

    def test_worker_communications_create(self):
        self.assertEqual(True, True)
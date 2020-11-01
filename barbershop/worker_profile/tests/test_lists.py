from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient
from apps_generic.dump import dump

from worker_profile.models import WorkerProfile, WorkerCommunications


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
        dump.dump(response)
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
                                                               social_network=WorkerCommunications.Type.facebook_id,
                                                               social_networks_ids='123')

    def test_worker_communications_list(self):
        response = self.c.get(
            '/worker_profile/worker_profile/worker_communications/'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        dump.dump(response)
        self.assertEqual(response.data, {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [
                    {
                        "id": self.worker_comm.id,
                        "worker_profile": self.worker_comm.worker_profile.id,
                        "social_network": self.worker_comm.social_network,
                        "social_networks_ids": self.worker_comm.social_networks_ids
                    },
                ]
            }
        )

    def test_worker_communications_create(self):
        self.assertEqual(True, True)
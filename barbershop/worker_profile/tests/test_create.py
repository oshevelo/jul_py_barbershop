from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient
from apps_generic.dump import dump

from worker_profile.models import WorkerProfile, WorkerCommunications


class WorkerProfileAndCommunicationsCreateAPITest(TestCase):
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
                'first_name': 'testtest',
                'second_name': 'testtesttest',
                'position': 'admin',
                'phone_number': '+222222222222',
                'email': 'testtesttesttest@gmail.com',
                'worker': self.user.id,
            },
            format='json'
        )

        dump.dump(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class WorkerCommunicationsListAPITest(TestCase):
    def setUp(self):
        self.c = APIClient()
        user_kw = dict(
            username='tt',
            password='111',
            email='tt' + '.com'
        )
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.worker = WorkerProfile.objects.create(first_name='test', second_name='testtest',
                                                   position='testbarber',
                                                   phone_number='+111111111111', email='test@gmail.com',
                                                   worker=self.user)

    def test_worker_communications_create(self):
        self.c.login(username='tt', password='111')
        response = self.c.post(
            '/worker_profile/worker_profile/worker_communications/',
            data={
                "worker_profile": 1,
                "social_network": WorkerCommunications.Type.facebook_id,
                "social_networks_ids": "@asdsa"
            },
            format='json'
        )
        dump.dump(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
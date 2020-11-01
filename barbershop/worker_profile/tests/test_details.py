from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient
from apps_generic.dump import dump

from worker_profile.models import WorkerProfile, WorkerCommunications


class WorkerProfileDetailsAPITest(TestCase):

    def setUp(self):
        self.c = APIClient()
        user_kw = dict(
            username='aa',
            password='aaa111',
            email='aaatt' + '.com'
        )
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.worker = WorkerProfile.objects.create(first_name='test', second_name='test', position='testbarber',
                                                   phone_number='+111111111111', email='test@gmail.com',
                                                   worker=self.user)

    def test_worker_profile_details(self):
        self.c.login(username='tt', password='111')

        response = self.c.get(
            '/worker_profile/worker_profile/1/'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        dump.dump(response)


class WorkerProfileDetailsPermissionAPITest(TestCase):

    def setUp(self):
        self.c = APIClient()
        user_kw1 = dict(
            username='aaa',
            password='aaa111',
            email='aaatt' + '.com'
        )
        user_kw1['password'] = make_password(user_kw1['password'])
        self.user1 = User.objects.create(**user_kw1)
        self.worker = WorkerProfile.objects.create(first_name='aaatest', second_name='aaatesttest',
                                                   position='aaatestbarber',
                                                   phone_number='+111111111111', email='aaatest@gmail.com',
                                                   worker=self.user1)
        user_kw2 = dict(
            username='tt2',
            password='222',
            email='tt2' + '.com'
        )
        user_kw2['password'] = make_password(user_kw2['password'])
        self.user2 = User.objects.create(**user_kw2)
        self.worker2 = WorkerProfile.objects.create(first_name='test2', second_name='testtest2', position='testbarber2',
                                                    phone_number='+222222222222', email='test2@gmail.com',
                                                    worker=self.user2)

    def test_worker_profile_details_permission(self):
        self.c.login(username='tt2', password='222')

        response = self.c.get(
            '/worker_profile/worker_profile/1/'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        dump.dump(response)


class WorkerCommunicationsListAPITest(TestCase):
    def setUp(self):
        self.c = APIClient()
        user_kw1 = dict(
            username='aaa',
            password='aaa111',
            email='aaatt' + '.com'
        )
        user_kw1['password'] = make_password(user_kw1['password'])
        self.user1 = User.objects.create(**user_kw1)
        self.worker = WorkerProfile.objects.create(first_name='test', second_name='testtest', position='testbarber',
                                                   phone_number='+111111111111', email='test@gmail.com',
                                                   worker=self.user1)
        self.worker_comm = WorkerCommunications.objects.create(worker_profile=self.worker,
                                                               social_network=WorkerCommunications.Type.facebook_id,
                                                               social_networks_ids='123')

        user_kw2 = dict(
            username='tt2',
            password='222',
            email='tt2' + '.com'
        )
        user_kw2['password'] = make_password(user_kw2['password'])
        self.user2 = User.objects.create(**user_kw2)
        self.worker2 = WorkerProfile.objects.create(first_name='test2', second_name='testtest2', position='testbarber2',
                                                    phone_number='+222222222222', email='test2@gmail.com',
                                                    worker=self.user2)
        self.worker_comm2 = WorkerCommunications.objects.create(worker_profile=self.worker2,
                                                                social_network=WorkerCommunications.Type.facebook_id,
                                                                social_networks_ids='2222')

    def test_worker_communications_details_permission(self):
        self.c.login(username='tt2', password='222')

        response = self.c.get(
            '/worker_profile/worker_profile/worker_communications/{}/'.format(self.worker_comm.id)
        )
        dump.dump(response)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

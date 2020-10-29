from django.test import TestCase
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient
from apps_generic.dump import dump

from worker_profile.models import WorkerProfile, WorkerCommunications


class WorkerProfileDeleteAPITest(TestCase):

    def setUp(self):
        self.c = APIClient()
        user_kw = dict(
            username='aa',
            password='aaa111',
            email='aaatt' + '.com'
        )
        user_kw['password'] = make_password(user_kw['password'])
        self.user = User.objects.create(**user_kw)
        self.worker = WorkerProfile.objects.create(first_name='test', second_name='testtest', position='testbarber',
                                                   phone_number='+111111111111', email='test@gmail.com',
                                                   worker=self.user)
        self.worker_comm = WorkerCommunications.objects.create(worker_profile=self.worker,
                                                               type=WorkerCommunications.Type.facebook_id,
                                                               social_networks_ids='123')

    def test_worker_profile_and_comm_delete(self):
        self.c.login(username='aa', password='aaa111')
        response = self.c.delete(
            '/worker_profile/worker_profile/{}/'.format(self.worker.id),
            # data={
            #     'id': self.user.id,
            #     'first_name': 'test',
            #     'second_name': 'testtestx',
            #     'position': 'testbarber',
            #     'phone_number': '+111111111111',
            #     'email': 'test@gmail.com',
            #     'worker': self.worker,
            # },
            # format='json'
        )

        dump.dump(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


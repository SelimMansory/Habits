from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from users.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            id=102,
            email='test@test.test',
            password='test',
            is_superuser=True,
            is_staff=True
        )
        self.client.force_authenticate(user=self.user)

    def test_destroy_user(self):
        """
        Тестирование удаление пользователя
        """
        response = self.client.delete(
            '/user/user/102/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_create_user(self):
        """
        Тестирование создания пользователя
        """
        response = self.client.post(
            '/user/create/',
            {'id': 52,
             'email': 'email@email.email',
             'password': 'test'}
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEquals(
            response.data['email'],
            'email@email.email'
        )

    def test_update_user(self):
        """
        Тестирование обновление пользователя
        """
        response = self.client.patch(
            '/user/user/102/',
            {'last_name': 'Semenov'}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEquals(
            response.data['last_name'],
            'Semenov'
        )

    def test_get_user(self):
        response = self.client.get(
            '/user/'
        )

        self.assertEquals(
            response.json(),
            [{
                'email': 'test@test.test',
                'phone': None,
                'first_name': '',
                'last_name': ''
            }]
        )
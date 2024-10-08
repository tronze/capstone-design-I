from rest_framework.test import APITestCase
from ..models import User
from rest_framework import status

class UserLoginTestCase(APITestCase):
    def setUp(self):
        self.url = '/users/token/'
        # 회원가입
        self.user = User.objects.create(
            email="logintest@example.com",
            name="logintest",
        )
        self.user.set_password("dkssud!!")
        self.user.save()

    def test_successful_login(self):
        user = {
            "email": "logintest@example.com",
            "password": "dkssud!!"
        }
        response = self.client.post(self.url, data=user, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wrong_password(self):
        user = {
            "email": "logintest@example.com",
            "password": "dkssyd!!"
        }
        response = self.client.post(self.url, data=user, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

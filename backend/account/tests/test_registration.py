from rest_framework.test import APITestCase
from ..factories import UserFactory
from rest_framework import status

class UserRegisterTestCase(APITestCase):
    def setUp(self):
        self.url = '/users/register/'

    def create_user_data(self, **kwargs):
        user = UserFactory.build() # db에 저장되지 않게 설정
        data = {
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "institution": user.institution,
            "password": user.password,
            "password2": user.password,
        }
        data.update(kwargs)
        return data

    def test_successful_registration(self):
        data = self.create_user_data()
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_with_duplicate_email(self):
        self.user = UserFactory.create()
        data = {
            "name": self.user.name, 
            "email": self.user.email,
            "role": self.user.role,
            "institution": self.user.institution,
            "password": self.user.password,
            "password2": self.user.password
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_invalid_email_format(self):
        data = self.create_user_data(email='abcemail@')
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_missing_name(self):
        data = self.create_user_data(name="")
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_register_with_short_password(self):
        data = self.create_user_data(password="a76", password2="a76")
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_mismatched_passwords(self):
        data = self.create_user_data(password="dkssud!!", password2="dkssyd!!")
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_missing_required_fields(self):
        data = self.create_user_data(name="", email="")
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_unselected_role(self):
        data = self.create_user_data(role="")
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
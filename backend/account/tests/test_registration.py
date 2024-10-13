from rest_framework.test import APITestCase
from ..factories import StudentFactory, TeacherFactory
from rest_framework import status
import random

class UserRegisterTestCase(APITestCase):
    def setUp(self):
        self.url = '/users/register/'

    def create_user_data(self, **kwargs):
        choice = random.choice([1, 2]) # 선생님과 학생 중 테스트할 모델을 랜덤으로 선택
        if choice == 1:
            user_factory = TeacherFactory
            user_type = "선생님"
        elif choice == 2:
            user_factory = StudentFactory
            user_type = "학생"
        user = user_factory.build() # db에 저장되지 않게 설정
        data = {
            "name": user.name,
            "email": user.email,
            "user_type": user_type,
            "password": user.password,
            "password2": user.password,
        }
        # 유저 타입에 따라 추가 필드 설정
        if user_type == '학생':
            data['school'] = user.school
            data['grade'] = user.grade
        elif user_type == '선생님':
            data['institution'] = user.institution
            data['subject'] = user.subject
        data.update(kwargs)
        return data

    def test_successful_registration(self):
        data = self.create_user_data()
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_with_duplicate_email(self):
        existing_user = self.create_user_data()
        self.client.post(self.url, data=existing_user, format='json')
        new_user = {
            "email": existing_user['email'],
            "name": "name",
            "password": "dkssud!!",
            "password2": "dkssud!!",
            "user_type": "학생",
            "school": "서강고", 
            "grade": "고3"
        }
        response = self.client.post(self.url, data=new_user, format='json')
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

    def test_register_with_unselected_fields(self):
        data = self.create_user_data()
        if data["user_type"] == "선생님":
            data["institution"] = None
            data["subject"] =  None
        elif data["user_type"] == "학생":
            data["school"] = None
            data["grade"] = None
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_with_invalid_user_type(self):
        data = self.create_user_data()
        data["user_type"] = "아뇨 뚱인데요"
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
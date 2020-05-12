"""Test Cases for auth api views
"""
from django.contrib.auth.models import User
from rest_framework_simplejwt.state import token_backend

from authenticate.tests.utils import APIViewTestCase


class TestAuthTokenObtainPairView(APIViewTestCase):
    """Tests for Auth Token Obtain Pair View
    """
    view_name = 'token_obtain_pair'

    def setUp(self):
        self.username = 'test_username'
        self.password = 'test_password'

        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_it_should_return_400_if_any_fields_missing(self):
        """Tests for missing fields
        """
        # empty data
        result = self.view_post(data={})
        self.assertEqual(result.status_code, 400)
        self.assertIn('username', result.data)
        self.assertIn('password', result.data)

        # username only
        result = self.view_post(data={
            'username': self.username
        })
        self.assertEqual(result.status_code, 400)
        self.assertIn('password', result.data)

        # password only
        result = self.view_post(data={
            'password': self.password
        })
        self.assertEqual(result.status_code, 400)
        self.assertIn('username', result.data)

    def test_it_should_return_401_if_credential_wrong(self):
        """Test for wrong credentials
        """
        result = self.view_post(data={
            'username': self.username,
            'password': 'test_password_wrong'
        })
        self.assertEqual(result.status_code, 401)
        self.assertIn('detail', result.data)

    def test_it_should_return_401_if_user_inactive(self):
        """Test when user is inactive
        """
        self.user.is_active = False
        self.user.save()

        result = self.view_post(data={
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(result.status_code, 401)
        self.assertIn('detail', result.data)

    def test_it_should_validate_when_payload_correct(self):
        """Test when payload is okay
        """
        user_attributes = [
            "username",
            "email",
        ]
        result = self.view_post(data={
            'username': self.username,
            'password': self.password
        })
        self.assertEqual(result.status_code, 200)
        self.assertIn('access', result.data["user"])
        self.assertIn('refresh', result.data["user"])

        payload = token_backend.decode(result.data["user"]['access'])
        for attributes in user_attributes:
            self.assertIn(attributes, payload)

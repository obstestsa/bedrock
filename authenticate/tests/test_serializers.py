"""Test Cases for auth-api serializers
"""
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import exceptions
from rest_framework_simplejwt.tokens import (
    AccessToken, RefreshToken,
)
from authenticate.serializers import AuthTokenObtainPairSerializer


class TestAuthTokenObtainPairSerializer(TestCase):
    """
    Tests for Token Obtain Serializer
    """

    def setUp(self):
        self.username = "test_user"
        self.password = "test_password"

        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )

    def test_it_should_not_validate_if_any_fields_missing(self):
        """
        Should not validate when any of the fields is not providded
        """
        # empty data
        serializer = AuthTokenObtainPairSerializer(data={})
        self.assertFalse(serializer.is_valid())

        # username only
        serializer = AuthTokenObtainPairSerializer(
            data={"username": "test_user_random"}
        )
        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

        # password only
        serializer = AuthTokenObtainPairSerializer(
            data={"password": "test_passwrod_random"}
        )
        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    def test_it_should_not_validate_if_user_not_found(self):
        """
        Exception should be raised when user is not found
        """
        serializer = AuthTokenObtainPairSerializer(
            data={
                "username": "test_user_random",
                "password": "test_password_random",
            }
        )

        with self.assertRaises(exceptions.AuthenticationFailed):
            serializer.is_valid()

    def test_it_should_raise_if_user_not_active(self):
        """
        Exception should be raised when user is not active
        """
        self.user.is_active = False
        self.user.save()

        serializer = AuthTokenObtainPairSerializer(
            data={"username": self.username, "password": self.password}
        )

        with self.assertRaises(exceptions.AuthenticationFailed):
            serializer.is_valid()

    def test_it_should_provide_a_token_when_data_valid(self):
        """
        Token should be provided with valid data
        """
        serializer = AuthTokenObtainPairSerializer(
            data={"username": self.username, "password": self.password}
        )

        self.assertTrue(serializer.is_valid())
        self.assertIn("access", serializer.validated_data.get("user"))
        self.assertIn("refresh", serializer.validated_data.get("user"))

    def test_it_should_provide_correct_token_subclass(self):
        """
        When token type is correct, intantiation of proper token subclass
        should not raise exception
        """
        serializer = AuthTokenObtainPairSerializer(
            data={"username": self.username, "password": self.password}
        )

        self.assertTrue(serializer.is_valid())

        # Should raise TokenError if invalid token type
        AccessToken(serializer.validated_data["user"]["access"])
        RefreshToken(serializer.validated_data["user"]["refresh"])

    def test_it_should_provide_extra_response_when_data_valid(self):
        """
        Extra responses should be provided with valid data
        """
        serializer = AuthTokenObtainPairSerializer(
            data={"username": self.username, "password": self.password}
        )

        self.assertTrue(serializer.is_valid())

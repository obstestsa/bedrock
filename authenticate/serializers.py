"""Serializers for auth api app
"""

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class AuthTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token["username"] = user.username
        token["email"] = user.email

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = data.pop("refresh")
        access = data.pop("access")
        data["user"] = {
            "username": self.user.username,
            "email": self.user.email,
            "refresh": refresh,
            "access": access,
        }
        return data

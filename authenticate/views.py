"""Views for auth api app
"""

from rest_framework_simplejwt.views import TokenObtainPairView
from authenticate.serializers import AuthTokenObtainPairSerializer

class AuthTokenObtainPairView(TokenObtainPairView):
    """Token Obtain Pair View

    """
    serializer_class = AuthTokenObtainPairSerializer

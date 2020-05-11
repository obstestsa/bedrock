"""URL config for auth api app
"""

from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authenticate.views import AuthTokenObtainPairView

urlpatterns = [
    path('token/', AuthTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

"""URL endpoints for SOR api app
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from sor.views import (
    LabelView,
    OwnerView,
    ClusterView,
    EnvironmentView,
    DomainView,
    OperatingSystemView,
    ServerView,
    ProductView,
)

ROUTER = DefaultRouter()
ROUTER.register(r"labels", LabelView)
ROUTER.register(r"owners", OwnerView)
ROUTER.register(r"clusters", ClusterView)
ROUTER.register(r"environments", EnvironmentView)
ROUTER.register(r"domains", DomainView)
ROUTER.register(r"operating_systems", OperatingSystemView)
ROUTER.register(r"servers", ServerView)
ROUTER.register(r"products", ProductView)

urlpatterns = [path("", include(ROUTER.urls))]

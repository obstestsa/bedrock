"""Views for SOR api app
"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from sor.models import (
    Label,
    Owner,
    Cluster,
    Environment,
    Domain,
    OperatingSystem,
    Server,
    Product,
)
from sor.serializers import (
    LabelSerializer,
    OwnerSerializer,
    ClusterSerializer,
    EnvironmentSerializer,
    DomainSerializer,
    OperatingSystemSerializer,
    ServerSerializer,
    ProductSerializer,
)


class LabelView(viewsets.ModelViewSet):
    """Rest view for Labels
    """

    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OwnerView(viewsets.ModelViewSet):
    """Rest view for Owners
    """

    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ClusterView(viewsets.ModelViewSet):
    """Rest view for Clusters
    """

    queryset = Cluster.objects.all()
    serializer_class = ClusterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class EnvironmentView(viewsets.ModelViewSet):
    """Rest view for Environment
    """

    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DomainView(viewsets.ModelViewSet):
    """Rest view for Domain
    """

    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OperatingSystemView(viewsets.ModelViewSet):
    """Rest view for OperatingSystem
    """

    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ServerView(viewsets.ModelViewSet):
    """Rest view for Server
    """

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductView(viewsets.ModelViewSet):
    """Rest view for Product
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

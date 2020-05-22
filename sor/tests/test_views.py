"""Test cases for sor views
"""

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

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


class LabelViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            "test", "test@example.com", "testpassword123"
        )
        cls.url = reverse("label-list")

    def setUp(self):
        self.client.force_authenticate(user=self.user)
        self.model_instance = Label.objects.create(name="test")

    def test_get_labels(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_a_label(self):
        data = {"name": "Another test"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Label.objects.all().count(), 1)
        self.assertEqual(
            Label.objects.get(name=data["name"]).name, data["name"]
        )

    def test_create_label_missing_field(self):
        data = {"invalid": "data test"}
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_a_label(self):
        data = {"name": "test updated"}
        response = self.client.put(f"{self.url}1/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Label.objects.get(id=1).name, data["name"])

    def test_update_invalid_label(self):
        data = {"name": "test updated"}
        response = self.client.put(f"{self.url}100/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_label(self):
        response = self.client.delete(f"{self.url}1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_remove_invalid_label(self):
        response = self.client.delete(f"{self.url}100/", format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class OwnerViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            "test", "test@example.com", "testpassword123"
        )
        cls.url = reverse("owner-list")

    def setUp(self):
        self.client.force_authenticate(user=self.user)
        self.model_instance = Owner.objects.create(
            name="test", email="test@example.com", description="A test owner"
        )

    def test_get_owners(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_a_owner(self):
        data = {
            "name": "test 2",
            "email": "test2@example.com",
            "description": "Another test owner",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Owner.objects.all().count(), 1)
        self.assertEqual(
            Owner.objects.get(name=data["name"]).name, data["name"]
        )

    def test_create_owner_missing_field(self):
        data = {
            "email": "test2@example.com",
            "description": "Another test owner",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_a_owner(self):
        data = {
            "name": "test Updated",
            "email": "test@example.com",
            "description": "A test owner",
        }
        response = self.client.put(f"{self.url}1/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Owner.objects.get(id=1).name, data["name"])

    def test_update_invalid_owner(self):
        data = {"name": "test updated"}
        response = self.client.put(f"{self.url}100/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_owner(self):
        response = self.client.delete(f"{self.url}1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_remove_invalid_owner(self):
        response = self.client.delete(f"{self.url}100/", format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ClusterViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            "test", "test@example.com", "testpassword123"
        )
        cls.url = reverse("cluster-list")

    def setUp(self):
        self.client.force_authenticate(user=self.user)
        self.model_instance = Cluster.objects.create(
            name="CLUSTERA", description="A test cluster"
        )

    def test_get_clusters(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_a_cluster(self):
        data = {
            "name": "CLUSTER B",
            "description": "A test cluster",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Cluster.objects.all().count(), 1)
        self.assertEqual(
            Cluster.objects.get(name=data["name"]).name, data["name"]
        )

    def test_create_cluster_missing_field(self):
        data = {
            "description": "A test cluster",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_a_cluster(self):
        data = {
            "name": "CLUSTERA Updated",
            "description": "A test cluster",
        }
        response = self.client.put(f"{self.url}1/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Cluster.objects.get(id=1).name, data["name"])

    def test_update_invalid_cluster(self):
        data = {
            "name": "CLUSTERA",
            "description": "A test cluster",
        }
        response = self.client.put(f"{self.url}100/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_cluster(self):
        response = self.client.delete(f"{self.url}1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_remove_invalid_cluster(self):
        response = self.client.delete(f"{self.url}100/", format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class EnvironmentViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            "test", "test@example.com", "testpassword123"
        )
        cls.url = reverse("environment-list")

    def setUp(self):
        self.client.force_authenticate(user=self.user)
        self.model_instance = Environment.objects.create(
            name="ENVA", category="DEV", description="Environment A"
        )

    def test_get_environments(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_a_environment(self):
        data = {
            "name": "ENVB",
            "category": "DEV",
            "description": "Environment B",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Environment.objects.all().count(), 1)
        self.assertEqual(
            Environment.objects.get(name=data["name"]).name, data["name"]
        )

    def test_create_environment_missing_field(self):
        data = {
            "category": "DEV",
            "description": "Environment B",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_a_environment(self):
        data = {
            "name": "ENVA Updated",
            "category": "DEV",
            "description": "Environment A",
        }
        response = self.client.put(f"{self.url}1/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Environment.objects.get(id=1).name, data["name"])

    def test_update_invalid_environment(self):
        data = {
            "name": "ENVB",
            "category": "DEV",
            "description": "Environment B",
        }
        response = self.client.put(f"{self.url}100/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_environment(self):
        response = self.client.delete(f"{self.url}1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_remove_invalid_environment(self):
        response = self.client.delete(f"{self.url}100/", format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class DomainViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            "test", "test@example.com", "testpassword123"
        )
        cls.url = reverse("domain-list")

    def setUp(self):
        self.client.force_authenticate(user=self.user)
        self.owner_instance = Owner.objects.create(
            name="OWNERA", email="owner@example.com", description="A owner"
        )
        self.model_instance = Domain.objects.create(
            name="domain.a",
            location="USA",
            owner=self.owner_instance,
            description="Domain A",
        )

    def test_get_domains(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_a_domain(self):
        data = {
            "description": "Domain B",
            "location": "USA",
            "name": "domain.b",
            "owner": "OWNERA",
            "status": "ACTIVE",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Domain.objects.all().count(), 1)
        self.assertEqual(
            Domain.objects.get(name=data["name"]).name, data["name"]
        )

    def test_create_domain_missing_field(self):
        data = {
            "description": "Domain B",
            "location": "USA",
            "owner": "OWNERA",
            "status": "ACTIVE",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_a_domain(self):
        data = {
            "description": "Domain A Updated",
            "location": "USA",
            "name": "domain.a",
            "owner": "OWNERA",
            "status": "ACTIVE",
        }
        response = self.client.put(f"{self.url}1/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Domain.objects.get(id=1).name, data["name"])

    def test_update_invalid_domain(self):
        data = {
            "description": "Domain A Updated",
            "location": "USA",
            "name": "domain.a",
            "owner": "OWNERA",
            "status": "ACTIVE",
        }
        response = self.client.put(f"{self.url}100/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_domain(self):
        response = self.client.delete(f"{self.url}1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_remove_invalid_domain(self):
        response = self.client.delete(f"{self.url}100/", format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class OperatingSystemViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            "test", "test@example.com", "testpassword123"
        )
        cls.url = reverse("operatingsystem-list")

    def setUp(self):
        self.client.force_authenticate(user=self.user)
        self.model_instance = OperatingSystem.objects.create(
            name="CENT OS", family="LINUX", architecture="64", version="8.0"
        )

    def test_get_operating_systems(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_a_operating_system(self):
        data = {
            "architecture": "64",
            "family": "LINUX",
            "name": "CENT OS 9",
            "version": "9.0",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(OperatingSystem.objects.all().count(), 1)
        self.assertEqual(
            OperatingSystem.objects.get(name=data["name"]).name, data["name"]
        )

    def test_create_operating_system_missing_field(self):
        data = {
            "architecture": "64",
            "family": "LINUX",
            "version": "8.0",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_a_operating_system(self):
        data = {
            "architecture": "64",
            "family": "LINUX",
            "name": "CENT OS Updated",
            "version": "8.0",
        }
        response = self.client.put(f"{self.url}1/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(OperatingSystem.objects.get(id=1).name, data["name"])

    def test_update_invalid_operating_system(self):
        data = {
            "architecture": "64",
            "family": "LINUX",
            "name": "CENT OS",
            "version": "8.0",
        }
        response = self.client.put(f"{self.url}100/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_operating_system(self):
        response = self.client.delete(f"{self.url}1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_remove_invalid_operating_system(self):
        response = self.client.delete(f"{self.url}100/", format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ServerViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            "test", "test@example.com", "testpassword123"
        )
        cls.url = reverse("server-list")

    def setUp(self):
        self.client.force_authenticate(user=self.user)
        self.owner_instance = Owner.objects.create(
            name="OWNERA", email="owner@example.com", description="A owner"
        )
        self.domain_instance = Domain.objects.create(
            name="domain.a",
            location="USA",
            owner=self.owner_instance,
            description="Domain A",
        )
        self.cluster_instance = Cluster.objects.create(
            name="CLUSTERA", description="A test cluster"
        )
        self.os_instance = OperatingSystem.objects.create(
            name="CENT OS", family="LINUX", architecture="64", version="8.0"
        )
        self.env_instance = Environment.objects.create(
            name="ENVA", category="DEV", description="Environment A"
        )
        self.label_instance = Label.objects.create(name="test")
        self.model_instance = Server.objects.create(
            name="testserverd1",
            ip_address="127.0.0.1",
            category="APP",
            owner=self.owner_instance,
            domain=self.domain_instance,
            cluster=self.cluster_instance,
            operating_system=self.os_instance,
            description="A test server",
            status="INACTIVE",
        )
        self.model_instance.environments.add(self.env_instance)
        self.model_instance.labels.add(self.label_instance)

    def test_get_servers(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_a_server(self):
        data = {
            "category": "APP",
            "cluster": "CLUSTERA",
            "description": "A test server",
            "domain": "domain.a",
            "environments": ["ENVA"],
            "ip_address": "127.0.0.2",
            "labels": ["test"],
            "name": "testserverd2",
            "operating_system": "CENT OS",
            "owner": "OWNERA",
            "status": "INACTIVE",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Server.objects.all().count(), 1)
        self.assertEqual(
            Server.objects.get(name=data["name"]).name, data["name"]
        )

    def test_create_server_missing_field(self):
        data = {
            "category": "APP",
            "cluster": "CLUSTERA",
            "description": "A test server",
            "domain": "domain.a",
            "environments": ["ENVA"],
            "ip_address": "127.0.0.2",
            "labels": ["test"],
            "operating_system": "CENT OS",
            "owner": "OWNERA",
            "status": "INACTIVE",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_a_server(self):
        data = {
            "category": "APP",
            "cluster": "CLUSTERA",
            "description": "A test server",
            "domain": "domain.a",
            "environments": ["ENVA"],
            "ip_address": "127.0.0.1",
            "labels": ["test"],
            "name": "testserverd1 Updated",
            "operating_system": "CENT OS",
            "owner": "OWNERA",
            "status": "INACTIVE",
        }
        response = self.client.put(f"{self.url}1/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Server.objects.get(id=1).name, data["name"])

    def test_update_invalid_server(self):
        data = {
            "category": "APP",
            "cluster": "CLUSTERA",
            "description": "A test server",
            "domain": "domain.a",
            "environments": ["ENVA"],
            "ip_address": "127.0.0.2",
            "labels": ["test"],
            "name": "testserverd2",
            "operating_system": "CENT OS",
            "owner": "OWNERA",
            "status": "INACTIVE",
        }
        response = self.client.put(f"{self.url}100/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_server(self):
        response = self.client.delete(f"{self.url}1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_remove_invalid_server(self):
        response = self.client.delete(f"{self.url}100/", format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ProductViewTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            "test", "test@example.com", "testpassword123"
        )
        cls.url = reverse("product-list")

    def setUp(self):
        self.client.force_authenticate(user=self.user)
        self.owner_instance = Owner.objects.create(
            name="OWNERA", email="owner@example.com", description="A owner"
        )
        self.model_instance = Product.objects.create(
            name="Product A",
            port="9000",
            version="2.0.1",
            owner=self.owner_instance,
            link="https://test.com",
            repository="https://test.com/repo",
        )

    def test_get_products(self):
        response = self.client.get(self.url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_a_product(self):
        data = {
            "link": "https://test.com",
            "name": "Product B",
            "owner": "OWNERA",
            "port": 9000,
            "repository": "https://test.com/repo",
            "version": "2.0.1",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Product.objects.all().count(), 1)
        self.assertEqual(
            Product.objects.get(name=data["name"]).name, data["name"]
        )

    def test_create_product_missing_field(self):
        data = {
            "link": "https://test.com",
            "owner": "OWNERA",
            "port": 9000,
            "repository": "https://test.com/repo",
            "version": "2.0.1",
        }
        response = self.client.post(self.url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_a_product(self):
        data = {
            "link": "https://test.com",
            "name": "Product A Updated",
            "owner": "OWNERA",
            "port": 9000,
            "repository": "https://test.com/repo",
            "version": "2.0.1",
        }
        response = self.client.put(f"{self.url}1/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get(id=1).name, data["name"])

    def test_update_invalid_product(self):
        data = {
            "link": "https://test.com",
            "name": "Product A Updated",
            "owner": "OWNERA",
            "port": 9000,
            "repository": "https://test.com/repo",
            "version": "2.0.1",
        }
        response = self.client.put(f"{self.url}100/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_remove_product(self):
        response = self.client.delete(f"{self.url}1/", format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_remove_invalid_product(self):
        response = self.client.delete(f"{self.url}100/", format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

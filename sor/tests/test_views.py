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

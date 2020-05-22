"""Test cases for sor models
"""

from django.test import TestCase

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


class LabelSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model_instance = Label.objects.create(name="test")

    def setUp(self):
        self.serializer = LabelSerializer(instance=self.model_instance)

    def test_label_serializer_contains_expected_fields(self):
        self.assertEqual(set(self.serializer.data.keys()), set(["id", "name"]))

    def test_label_serializer_give_expected_output(self):
        self.assertEqual(self.serializer.data.get("name"), "test")

    def test_label_serializer_is_valid_on_correct_data(self):
        data = {"name": "test"}
        serializer = LabelSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.data, data)

    def test_label_serializer_is_invalid_on_incorrect_data(self):
        data = {"random": "test"}
        serializer = LabelSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertNotEqual(serializer.data, data)


class OwnerSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model_instance = Owner.objects.create(
            name="test", email="test@example.com", description="A test owner"
        )

    def setUp(self):
        self.serializer = OwnerSerializer(instance=self.model_instance)

    def test_owner_serializer_contains_expected_fields(self):
        self.assertEqual(
            set(self.serializer.data.keys()),
            set(["id", "name", "email", "description"]),
        )

    def test_owner_serializer_give_expected_output(self):
        valid_data = {
            "id": 1,
            "name": "test",
            "email": "test@example.com",
            "description": "A test owner",
        }
        self.assertDictEqual(self.serializer.data, valid_data)

    def test_owner_serializer_is_valid_on_correct_data(self):
        data = {
            "name": "test",
            "email": "test@example.com",
            "description": "A test owner",
        }
        serializer = OwnerSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.data, data)

    def test_owner_serializer_is_invalid_on_incorrect_data(self):
        data = {"random": "test"}
        serializer = OwnerSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertNotEqual(serializer.data, data)


class ClusterSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model_instance = Cluster.objects.create(
            name="CLUSTERA", description="A test cluster"
        )

    def setUp(self):
        self.serializer = ClusterSerializer(instance=self.model_instance)

    def test_cluster_serializer_contains_expected_fields(self):
        self.assertEqual(
            set(self.serializer.data.keys()),
            set(["id", "name", "description"]),
        )

    def test_cluster_serializer_give_expected_output(self):
        valid_data = {
            "id": 1,
            "name": "CLUSTERA",
            "description": "A test cluster",
        }
        self.assertDictEqual(self.serializer.data, valid_data)

    def test_cluster_serializer_is_valid_on_correct_data(self):
        data = {
            "name": "CLUSTERA",
            "description": "A test cluster",
        }
        serializer = ClusterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.data, data)

    def test_cluster_serializer_is_invalid_on_incorrect_data(self):
        data = {"random": "test"}
        serializer = ClusterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertNotEqual(serializer.data, data)


class EnvironmentSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model_instance = Environment.objects.create(
            name="ENVA", category="DEV", description="Environment A"
        )

    def setUp(self):
        self.serializer = EnvironmentSerializer(instance=self.model_instance)

    def test_environment_serializer_contains_expected_fields(self):
        self.assertEqual(
            set(self.serializer.data.keys()),
            set(["id", "name", "category", "description"]),
        )

    def test_environment_serializer_give_expected_output(self):
        valid_data = {
            "id": 1,
            "name": "ENVA",
            "category": "DEV",
            "description": "Environment A",
        }
        self.assertDictEqual(self.serializer.data, valid_data)

    def test_environment_serializer_is_valid_on_correct_data(self):
        data = {
            "name": "ENVA",
            "category": "DEV",
            "description": "Environment A",
        }
        serializer = EnvironmentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.data, data)

    def test_environment_serializer_is_invalid_on_incorrect_data(self):
        data = {"random": "test"}
        serializer = EnvironmentSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertNotEqual(serializer.data, data)


class DomainSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.owner_instance = Owner.objects.create(
            name="OWNERA", email="owner@example.com", description="A owner"
        )
        cls.model_instance = Domain.objects.create(
            name="domain.a",
            location="USA",
            owner=cls.owner_instance,
            description="Domain A",
        )

    def setUp(self):
        self.serializer = DomainSerializer(instance=self.model_instance)

    def test_domain_serializer_contains_expected_fields(self):
        self.assertEqual(
            set(self.serializer.data.keys()),
            set(["id", "name", "location", "owner", "description", "status"]),
        )

    def test_domain_serializer_give_expected_output(self):
        valid_data = {
            "description": "Domain A",
            "id": 1,
            "location": "USA",
            "name": "domain.a",
            "owner": "OWNERA",
            "status": "ACTIVE",
        }
        self.assertDictEqual(self.serializer.data, valid_data)

    def test_domain_serializer_is_valid_on_correct_data(self):
        data = {
            "description": "Domain A",
            "location": "USA",
            "name": "domain.a",
            "owner": "OWNERA",
            "status": "ACTIVE",
        }
        serializer = DomainSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.data, data)

    def test_domain_serializer_is_invalid_on_incorrect_data(self):
        data = {"random": "test"}
        serializer = DomainSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertNotEqual(serializer.data, data)


class OperatingSystemSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model_instance = OperatingSystem.objects.create(
            name="CENT OS", family="LINUX", architecture="64", version="8.0"
        )

    def setUp(self):
        self.serializer = OperatingSystemSerializer(
            instance=self.model_instance
        )

    def test_operating_system_serializer_contains_expected_fields(self):
        self.assertEqual(
            set(self.serializer.data.keys()),
            set(["id", "name", "family", "architecture", "version"]),
        )

    def test_operating_system_serializer_give_expected_output(self):
        valid_data = {
            "architecture": "64",
            "family": "LINUX",
            "id": 1,
            "name": "CENT OS",
            "version": "8.0",
        }
        self.assertDictEqual(self.serializer.data, valid_data)

    def test_operating_system_serializer_is_valid_on_correct_data(self):
        data = {
            "architecture": "64",
            "family": "LINUX",
            "name": "CENT OS",
            "version": "8.0",
        }
        serializer = OperatingSystemSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertDictEqual(serializer.data, data)

    def test_operating_system_serializer_is_invalid_on_incorrect_data(self):
        data = {"random": "test"}
        serializer = OperatingSystemSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertNotEqual(serializer.data, data)


class ServerSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.owner_instance = Owner.objects.create(
            name="OWNERA", email="owner@example.com", description="A owner"
        )
        cls.domain_instance = Domain.objects.create(
            name="domain.a",
            location="USA",
            owner=cls.owner_instance,
            description="Domain A",
        )
        cls.cluster_instance = Cluster.objects.create(
            name="CLUSTERA", description="A test cluster"
        )
        cls.os_instance = OperatingSystem.objects.create(
            name="CENT OS", family="LINUX", architecture="64", version="8.0"
        )
        cls.env_instance = Environment.objects.create(
            name="ENVA", category="DEV", description="Environment A"
        )
        cls.label_instance = Label.objects.create(name="test")
        cls.model_instance = Server.objects.create(
            name="testserverd1",
            ip_address="127.0.0.1",
            category="APP",
            owner=cls.owner_instance,
            domain=cls.domain_instance,
            cluster=cls.cluster_instance,
            operating_system=cls.os_instance,
            description="A test server",
            status="INACTIVE",
        )
        cls.model_instance.environments.add(cls.env_instance)
        cls.model_instance.labels.add(cls.label_instance)

    def setUp(self):
        self.serializer = ServerSerializer(instance=self.model_instance)

    def test_server_serializer_contains_expected_fields(self):
        self.assertEqual(
            set(self.serializer.data.keys()),
            set(
                [
                    "id",
                    "name",
                    "ip_address",
                    "category",
                    "owner",
                    "domain",
                    "cluster",
                    "environments",
                    "operating_system",
                    "labels",
                    "description",
                    "status",
                ]
            ),
        )

    def test_server_serializer_give_expected_output(self):
        valid_data = {
            "category": "APP",
            "cluster": "CLUSTERA",
            "description": "A test server",
            "domain": "domain.a",
            "environments": ["ENVA"],
            "id": 1,
            "ip_address": "127.0.0.1",
            "labels": ["test"],
            "name": "testserverd1",
            "operating_system": "CENT OS",
            "owner": "OWNERA",
            "status": "INACTIVE",
        }
        self.assertDictEqual(self.serializer.data, valid_data)

    def test_server_serializer_is_valid_on_correct_data(self):
        data = {
            "category": "APP",
            "cluster": "CLUSTERA",
            "description": "A test server",
            "domain": "domain.a",
            "environments": ["ENVA"],
            "ip_address": "127.0.0.1",
            "labels": ["test"],
            "name": "testserverd1",
            "operating_system": "CENT OS",
            "owner": "OWNERA",
            "status": "INACTIVE",
        }
        serializer = ServerSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.data, data)

    def test_server_serializer_is_invalid_on_incorrect_data(self):
        data = {"random": "test"}
        serializer = ServerSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertNotEqual(serializer.data, data)


class ProductSerializerTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.owner_instance = Owner.objects.create(
            name="OWNERA", email="owner@example.com", description="A owner"
        )
        cls.model_instance = Product.objects.create(
            name="Product A",
            port="9000",
            version="2.0.1",
            owner=cls.owner_instance,
            link="https://test.com",
            repository="https://test.com/repo",
        )

    def setUp(self):
        self.serializer = ProductSerializer(instance=self.model_instance)

    def test_product_serializer_contains_expected_fields(self):
        self.assertEqual(
            set(self.serializer.data.keys()),
            set(
                [
                    "id",
                    "name",
                    "port",
                    "version",
                    "owner",
                    "link",
                    "repository",
                ]
            ),
        )

    def test_product_serializer_give_expected_output(self):
        valid_data = {
            "id": 1,
            "link": "https://test.com",
            "name": "Product A",
            "owner": "OWNERA",
            "port": 9000,
            "repository": "https://test.com/repo",
            "version": "2.0.1",
        }
        self.assertDictEqual(self.serializer.data, valid_data)

    def test_product_serializer_is_valid_on_correct_data(self):
        data = {
            "link": "https://test.com",
            "name": "Product A",
            "owner": "OWNERA",
            "port": 9000,
            "repository": "https://test.com/repo",
            "version": "2.0.1",
        }
        serializer = ProductSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertDictEqual(serializer.data, data)

    def test_product_serializer_is_invalid_on_incorrect_data(self):
        data = {"random": "test"}
        serializer = ProductSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertNotEqual(serializer.data, data)

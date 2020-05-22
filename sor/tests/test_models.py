"""Test cases for sor models
"""

from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
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


class LabelModelTestCase(TestCase):
    """Test for label models CRUD and more
    """

    @classmethod
    def setUpTestData(cls):
        cls.model_instance = Label.objects.create(name="test")

    def test_label_verbose_name(self):
        """Test labels verbose name
        """
        self.assertEqual(Label._meta.verbose_name, "Label")
        self.assertEqual(Label._meta.verbose_name_plural, "Labels")

    def test_label_create(self):
        """Test label can be created
        """
        label = Label.objects.create(name="hello")
        self.assertIsInstance(label, Label)
        self.assertEqual(label.__str__(), label.name)

    def test_label_instance_is_correct(self):
        """Test label model is working as exected
        """
        self.assertEqual(self.model_instance.name, "test")

    def test_label_is_updated(self):
        """Test Label can be updated
        """
        setattr(self.model_instance, "name", "test_updated")
        self.assertEqual(self.model_instance.name, "test_updated")

    def test_label_is_destroyed(self):
        """Test Label can be deleted
        """
        self.model_instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(name="test")


class OwnerModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model_instance = Owner.objects.create(
            name="test", email="test@example.com", description="A test owner"
        )

    def test_owner_verbose_name(self):
        """Test owner verbose name
        """
        self.assertEqual(Owner._meta.verbose_name, "Owner")
        self.assertEqual(Owner._meta.verbose_name_plural, "Owners")

    def test_owner_create(self):
        """Test owner can be created
        """
        a_owner = Owner.objects.create(
            name="a owner", email="a-owner@example.com", description="A owner"
        )
        self.assertIsInstance(a_owner, Owner)
        self.assertEqual(a_owner.__str__(), a_owner.name)
        self.assertEqual(a_owner.name, "a owner")

    def test_owner_is_updated(self):
        """Test owner can be updated
        """
        setattr(self.model_instance, "name", "test_updated")
        self.assertEqual(self.model_instance.name, "test_updated")

    def test_owner_is_destroyed(self):
        """Test owner can be remvoed
        """
        self.model_instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Owner.objects.get(name="test")


class ClusterModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model_instance = Cluster.objects.create(
            name="CLUSTERA", description="A test cluster"
        )

    def test_cluster_verbose_name(self):
        """Test cluster verbose name
        """
        self.assertEqual(Cluster._meta.verbose_name, "Cluster")
        self.assertEqual(Cluster._meta.verbose_name_plural, "Clusters")

    def test_cluster_create(self):
        """Test cluster can be created
        """
        b_cluster = Cluster.objects.create(
            name="CLUSTERB", description="Cluster B"
        )
        self.assertIsInstance(b_cluster, Cluster)
        self.assertEqual(b_cluster.__str__(), b_cluster.name)
        self.assertEqual(b_cluster.name, "CLUSTERB")

    def test_cluster_is_updated(self):
        """Test cluster can be updated
        """
        setattr(self.model_instance, "name", "CLUSTERA_updated")
        self.assertEqual(self.model_instance.name, "CLUSTERA_updated")

    def test_cluster_is_destroyed(self):
        """Test cluster can be removed
        """
        self.model_instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Cluster.objects.get(name="CLUSTERA")


class EnvironmentModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model_instance = Environment.objects.create(
            name="ENVA", category="DEV", description="Environment A"
        )

    def test_environment_verbose_name(self):
        """Test environment verbose name
        """
        self.assertEqual(Environment._meta.verbose_name, "Environment")
        self.assertEqual(Environment._meta.verbose_name_plural, "Environments")

    def test_environment_create(self):
        """Test environment can be created
        """
        b_environment = Environment.objects.create(
            name="ENVB", category="BETA", description="Environment B"
        )
        self.assertIsInstance(b_environment, Environment)
        self.assertEqual(b_environment.__str__(), b_environment.name)
        self.assertEqual(b_environment.name, "ENVB")

    def test_environment_is_updated(self):
        """Test environment can be updated
        """
        setattr(self.model_instance, "name", "ENVA_updated")
        self.assertEqual(self.model_instance.name, "ENVA_updated")

    def test_environment_is_destroyed(self):
        """Test environment can be removed
        """
        self.model_instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Environment.objects.get(name="ENVA")


class DomainModelTestCase(TestCase):
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

    def test_domain_verbose_name(self):
        """Test domain verbose name
        """
        self.assertEqual(Domain._meta.verbose_name, "Domain")
        self.assertEqual(Domain._meta.verbose_name_plural, "Domains")

    def test_domain_create(self):
        """Test domain can be created
        """
        b_domain = Domain.objects.create(
            name="domain.b",
            location="Canada",
            owner=self.owner_instance,
            description="Domain B",
        )
        self.assertIsInstance(b_domain, Domain)
        self.assertEqual(b_domain.__str__(), b_domain.name)
        self.assertEqual(b_domain.name, "domain.b")

    def test_domain_is_updated(self):
        """Test domain can be updated
        """
        setattr(self.model_instance, "name", "domain.a.updated")
        self.assertEqual(self.model_instance.name, "domain.a.updated")

    def test_domain_is_destroyed(self):
        """Test domain can be removed
        """
        self.model_instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Domain.objects.get(name="domain.a")


class OperatingSystemModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.model_instance = OperatingSystem.objects.create(
            name="CENT OS", family="LINUX", architecture="64", version="8.0"
        )

    def test_operating_system_verbose_name(self):
        """Test operating_system verbose name
        """
        self.assertEqual(
            OperatingSystem._meta.verbose_name, "Operating System"
        )
        self.assertEqual(
            OperatingSystem._meta.verbose_name_plural, "Operating Systems"
        )

    def test_operating_system_create(self):
        """Test operating_system can be created
        """
        b_operating_system = OperatingSystem.objects.create(
            name="CENT OS B", family="LINUX", architecture="64", version="8.0"
        )
        self.assertIsInstance(b_operating_system, OperatingSystem)
        self.assertEqual(b_operating_system.__str__(), b_operating_system.name)
        self.assertEqual(b_operating_system.name, "CENT OS B")

    def test_operating_system_is_updated(self):
        """Test operating_system can be updated
        """
        setattr(self.model_instance, "name", "CENT OS B updated")
        self.assertEqual(self.model_instance.name, "CENT OS B updated")

    def test_operating_system_is_destroyed(self):
        """Test operating_system can be removed
        """
        self.model_instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            OperatingSystem.objects.get(name="CENT OS")


class ServerModelTestCase(TestCase):
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

    def test_server_verbose_name(self):
        """Test server verbose name
        """
        self.assertEqual(Server._meta.verbose_name, "Server")
        self.assertEqual(Server._meta.verbose_name_plural, "Servers")

    def test_server_create(self):
        """Test server can be created
        """
        b_server = Server.objects.create(
            name="testserverd2",
            ip_address="127.0.0.2",
            category="APP",
            owner=self.owner_instance,
            domain=self.domain_instance,
            cluster=self.cluster_instance,
            operating_system=self.os_instance,
            description="A test server 2",
            status="INACTIVE",
        )
        self.model_instance.environments.add(self.env_instance)
        self.model_instance.labels.add(self.label_instance)

        self.assertIsInstance(b_server, Server)
        self.assertEqual(b_server.__str__(), b_server.name)
        self.assertEqual(b_server.name, "testserverd2")

    def test_server_is_updated(self):
        """Test server can be updated
        """
        setattr(self.model_instance, "name", "testserverd1_updated")
        self.assertEqual(self.model_instance.name, "testserverd1_updated")

    def test_server_is_destroyed(self):
        """Test server can be removed
        """
        self.model_instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Server.objects.get(name="testserverd1")


class ProductModelTestCase(TestCase):
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

    def test_product_verbose_name(self):
        """Test product verbose name
        """
        self.assertEqual(Product._meta.verbose_name, "Product")
        self.assertEqual(Product._meta.verbose_name_plural, "Products")

    def test_product_create(self):
        """Test product can be created
        """
        b_product = Product.objects.create(
            name="Product B",
            port="9000",
            version="2.0.1",
            owner=self.owner_instance,
            link="https://test.com",
            repository="https://test.com/repo",
        )
        self.assertIsInstance(b_product, Product)
        self.assertEqual(b_product.__str__(), b_product.name)
        self.assertEqual(b_product.name, "Product B")

    def test_product_is_updated(self):
        """Test product can be updated
        """
        setattr(self.model_instance, "name", "Product A_updated")
        self.assertEqual(self.model_instance.name, "Product A_updated")

    def test_product_is_destroyed(self):
        """Test product can be removed
        """
        self.model_instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Product.objects.get(name="Product A")

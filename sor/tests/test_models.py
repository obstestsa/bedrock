"""Test cases for sor models
"""

from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from sor.models import Label, Owner, Cluster, Environment, Domain


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
        setattr(self.model_instance, "name", "test_updated")
        self.assertEqual(self.model_instance.name, "test_updated")

    def test_label_is_destroyed(self):
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

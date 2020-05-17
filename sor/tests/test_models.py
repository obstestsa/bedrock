"""Test cases for sor models
"""

from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from sor.models import Label, Owner


class LabelTestCase(TestCase):
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

def OwnerTestCase(TestCase):

    def setUpTestData(cls):
        cls.model_instance = Owner.objects.create(
            name="test"
            email="test@example.com"
            description="A test owner"
        )

    def test_owner_verbose_name(self):
        self.assertEqual(Owner._meta.verbose_name, "Owner")
        self.assertEqual(Owner._meta.verbose_name_plural, "Owners")
    
    def test_owner_create(self):
        a_owner = Owner.objects.create(
            name="a owner"
            email="a-owner@example.com"
            description="A owner"
        )
        self.assertIsInstance(a_owner, Owner)
        self.assertEqual(a_owner.__str__(), a_owner.name)
        self.assertEqual(a_owner.name, "a owner")
    
    def test_owner_is_updated(self):
        setattr(self.model_instance, "name", "test_updated")
        self.assertEqual(self.model_instance.name, "test_updated")

    def test_owner_is_destroyed(self):
        self.model_instance.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Owner.object.get(name="test")
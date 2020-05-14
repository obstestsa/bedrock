"""Test cases for sor models
"""

from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from sor.models import Label


class LabelModelTestCase(TestCase):
    """Test for label models CRUD and more
    """

    @classmethod
    def setUpTestData(cls):
        cls.label_test = Label.objects.create(name="test")

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
        self.assertEqual(self.label_test.name, "test")

    def test_label_is_updated(self):
        setattr(self.label_test, "name", "test_updated")
        self.assertEqual(self.label_test.name, "test_updated")

    def test_label_is_destroyed(self):
        self.label_test.delete()

        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(name="test")

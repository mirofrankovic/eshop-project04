from django.test import TestCase
from .models import Product

class TestProductModel(TestCase):

    def test_create_product(self):
        product = Product(name="CocaCola", description='Some test content description.')
        self.assertEqual(product.name, 'CocaCola')
        self.assertEqual(product.description, "Some test content description.")
        self.assertEqual(product.year_warranty, '1');

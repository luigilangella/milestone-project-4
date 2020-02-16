from django.test import TestCase
from .models import Catalog, CatalogCategory, Product, ProductDetail, ProductAttribute, Preference

class TestCatalog(TestCase):
    def test_str_catalog(self):
        new_catalog = Catalog(name='winter')
        self.assertEqual(new_catalog.name, 'winter')

class TestCatalogCategory(TestCase):
    def test_str_catalog_category(self):
        new_catalog_category = CatalogCategory(name='food and drinks')
        self.assertEqual(new_catalog_category.name, 'food and drinks')

class TestProduct(TestCase):
    def test_str_product(self):
        new_product = Product(name='salame')
        self.assertEqual(new_product.name, 'salame')

class TestProductDetail(TestCase):
    def test_str_detail(self):
        new_product_detail = ProductDetail(description='abv%', value=12.5)
        self.assertEqual(new_product_detail.description, 'abv%')
        self.assertEqual(new_product_detail.value, 12.5)

class TestProductAttribute(TestCase):
    def test_str_attribute(self):
        new_product_attribute = ProductAttribute(name='red wine')
        self.assertEqual(new_product_attribute.name, 'red wine')

class TestPreference(TestCase):
    def test_str_preference(self):
        new_preference = Preference(value=1)
        self.assertEqual(new_preference.value, 1)


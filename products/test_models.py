from django.test import TestCase
from .models import Catalog, CatalogCategory, Product, ProductDetail, ProductAttribute, Preference, User

class TestCatalog(TestCase):
    """ A simple test to assert that Catalog model works as expected. """
    def test_str_catalog(self):
        new_catalog = Catalog(name='winter')
        self.assertEqual('winter', str(new_catalog))

class TestCatalogCategory(TestCase):
    """ A simple test to assert that CatalogCategory model works as expected. """
    def test_str_catalog_category(self):
        catalog = Catalog(name='winter')
        parent = CatalogCategory(name='food')
        new_catalog_category = CatalogCategory(name='food and drinks', catalog=catalog, parent=parent)
        new_catalog_category_two = CatalogCategory(name='food and drinks', catalog=catalog)
        self.assertEqual(
            new_catalog_category.__str__(), str(new_catalog_category.catalog.name) + ' : ' + str(new_catalog_category.parent.name) + ' - ' + str(new_catalog_category.name)
        )
        
        self.assertEqual(
            new_catalog_category_two.__str__(), str(new_catalog_category_two.catalog.name) + ' : ' + str(new_catalog_category_two.name)
        )

class TestProduct(TestCase):
    """ A simple test to assert that Product model works as expected. """
    def test_str_product(self):
        new_product = Product(name='salame')
        self.assertEqual('salame', str(new_product))

class TestProductDetail(TestCase):
    """ A simple test to assert that ProductDetail model works as expected. """
    def test_str_detail(self):
        product = Product(name='wine')
        attribute = ProductAttribute(name='abv%')
        new_product_detail = ProductDetail(product=product, attribute=attribute, value='12.5')
        self.assertEqual(new_product_detail.__str__(), (str(new_product_detail.product) + ' : ' + str(new_product_detail.attribute) + ' - ' + str(new_product_detail.value)))

class TestProductAttribute(TestCase):
    """ A simple test to assert that ProductAttribute model works as expected. """
    def test_str_attribute(self):
        new_product_attribute = ProductAttribute(name='red wine')
        self.assertEqual('red wine', str(new_product_attribute))

class TestPreference(TestCase):
    """ A simple test to assert that Preference model works as expected. """
    def test_str_preference(self):
        user = User(username='luigi')
        product = Product(name='wine')
        new_preference = Preference(user=user, product=product, value=1)
        self.assertEqual(new_preference.__str__(), (str(new_preference.user.username + ':' + str(new_preference.product) + ':' + str(new_preference.value))))


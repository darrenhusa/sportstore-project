from django.test import TestCase

from store.models import Product

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Product.objects.create(name='Football', description='blah blah blah', \
                               price=25, category='Sporting Goods')

    def test_name_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEquals(field_label, 'price')

    def test_category_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('category').verbose_name
        self.assertEquals(field_label, 'category')

    def test_name_help_text(self):
        product = Product.objects.get(id=1)
        field_help_text = product._meta.get_field('name').help_text
        expected_text = 'Enter the product name.'
        self.assertEquals(field_help_text, expected_text)

    def test_description_help_text(self):
        product = Product.objects.get(id=1)
        field_help_text = product._meta.get_field('description').help_text
        expected_text = 'Enter the product description.'
        self.assertEquals(field_help_text, expected_text)

    def test_price_help_text(self):
        product = Product.objects.get(id=1)
        field_help_text = product._meta.get_field('price').help_text
        expected_text = 'Enter the product price.'
        self.assertEquals(field_help_text, expected_text)

    def test_category_help_text(self):
        product = Product.objects.get(id=1)
        field_help_text = product._meta.get_field('category').help_text
        expected_text = 'Enter the product category.'
        self.assertEquals(field_help_text, expected_text)



    def test_name_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_description_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('description').max_length
        self.assertEquals(max_length, 100)

    def test_category_max_length(self):
        product = Product.objects.get(id=1)
        max_length = product._meta.get_field('category').max_length
        self.assertEquals(max_length, 50)

    def test_get_absolute_url(self):
        product = Product.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(product.get_absolute_url(), '/store/product/1')

    def test_object_name_is_name(self):
            product = Product.objects.get(id=1)
            expected_object_name = f'{product.name}'
            self.assertEquals(expected_object_name, str(product))

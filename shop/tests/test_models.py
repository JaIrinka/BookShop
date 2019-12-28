from django.test import TestCase
from shop.models import Publisher, Book, Shop, Catalog


class PublisherModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Publisher.objects.create(name='p12')

    def test_name_label(self):
        publisher = Publisher.objects.get(id=1)
        field_label = publisher._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        publisher = Publisher.objects.get(id=1)
        max_length = publisher._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Publisher.objects.create(name='p12')
        Book.objects.create(title='b12', publisher=Publisher.objects.get(id=1))

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length, 50)


class ShopModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Publisher.objects.create(name='p12')
        Book.objects.create(title='b12', publisher=Publisher.objects.get(id=1))
        Shop.objects.create(name='s1')

    def test_name_label(self):
        shop = Shop.objects.get(id=1)
        field_label = shop._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_title_max_length(self):
        shop = Shop.objects.get(id=1)
        max_length = shop._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)


class CatalogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Publisher.objects.create(name='p12')
        Book.objects.create(title='b12', publisher=Publisher.objects.get(id=1))
        Shop.objects.create(name='s1')
        Catalog.objects.create(count=3, book=Book.objects.get(id=1), shop=Shop.objects.get(id=1))

    def test_name_label(self):
        catalog = Catalog.objects.get(id=1)
        field_label = catalog._meta.get_field('count').verbose_name
        self.assertEquals(field_label, 'count')


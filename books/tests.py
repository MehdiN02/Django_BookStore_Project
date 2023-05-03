from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookShopTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book1 = Book.objects.create(
            title='book_test_1',
            author='mahdi',
            content='this is my book 1',
            price=12.50,
        )
        cls.book2 = Book.objects.create(
            title='book_test_2',
            author='mehdi',
            content='this is my book 2',
            price=15.99,
        )

    def test_book_model_srt(self):
        book = self.book1
        self.assertEqual(str(book), book.title)

    def test_book_detail(self):
        self.assertEqual(self.book1.title, 'book_test_1')
        self.assertEqual(self.book1.content, 'this is my book 1')
        self.assertEqual(self.book1.author, 'mahdi')

    def test_book_list_url(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_book_list_url_by_name(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_title_on_book_list(self):
        response = self.client.get(reverse('book_list'))
        self.assertContains(response, self.book2.title)

    def test_book_detail_url(self):
        response = self.client.get(f'/books/{self.book1.id}/')  # jostojo dar safhe book_list baraye id book sakhte
        # shode
        self.assertEqual(response.status_code, 200)

    def test_book_detail_url_by_name(self):
        response = self.client.get(reverse('book_detail', args=[self.book2.id]))
        self.assertEqual(response.status_code, 200)

    def test_book_details_on_book_detail_page(self):
        response = self.client.get(reverse('book_detail', args=[self.book1.id]))
        self.assertContains(response, self.book1.title)
        self.assertContains(response, self.book1.content)

    def test_status_404_if_book_dos_not_exist(self):
        response = self.client.get(reverse('book_detail', args=[1050]))
        self.assertEqual(response.status_code, 404)

    def test_book_create_view(self):
        response = self.client.post(reverse('book_create'), {
            'title': 'book_test_create',
            'author': 'mm',
            'content': 'this is book test create view',
            'price': 25.98,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.last().title, 'book_test_create')
        self.assertEqual(Book.objects.last().content, 'this is book test create view')

    def test_book_delete_view(self):
        response = self.client.post(reverse('book_delete', args=[self.book1.id]))
        self.assertEqual(response.status_code, 302)

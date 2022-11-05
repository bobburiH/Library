from django.test import TestCase
from django.urls import reverse
from .models import Book


class BookTests(TestCase):
    @classmethod
    def setUp(cls):
        cls.book = Book.objects.create(title="A good title",
                                       subtitle='bad subtitle',
                                       author='auth',
                                       isbn='1234567891234')

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtitle, 'bad subtitle')
        self.assertEqual(self.book.author, "auth")
        self.assertEqual(self.book.isbn, "1234567891234")

    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "subtitle")
        self.assertTemplateUsed(response, "book_list.html")

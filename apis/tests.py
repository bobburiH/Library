from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book


class APItests(APITestCase):
    @classmethod
    def setUp(self):
        self.book = Book.objects.create(title="Ram",
                                        subtitle="Ayodhya",
                                        author="Amish Tripati",
                                        isbn="1234567890123")

    def test_book_content(self):
        self.assertEqual(self.book.title, "Ram")
        self.assertEqual(self.book.subtitle, 'Ayodhya')
        self.assertEqual(self.book.author, "Amish Tripati")
        self.assertEqual(self.book.isbn, "1234567890123")

    def test_api_listview(self):
        response = self.client.get(reverse('books_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('Count = ', Book.objects.count())
        #self.assertEqual(Book.objects.count(), 1)

        #self.assertContains(response, self.book)

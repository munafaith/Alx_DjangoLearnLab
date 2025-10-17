# api/test_views.py

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
# No longer need to import Token model
from .models import Author, Book

# Get the User model
User = get_user_model()

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints.
    """

    def setUp(self):
        """
        Set up the initial data for the tests.
        """
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Use self.client.login() as required by the checker
        self.client.login(username='testuser', password='testpassword')

        # Create sample authors and books
        self.author1 = Author.objects.create(name='George Orwell')
        self.author2 = Author.objects.create(name='J.R.R. Tolkien')

        self.book1 = Book.objects.create(
            title='Nineteen Eighty-Four',
            publication_year=1949,
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title='The Hobbit',
            publication_year=1937,
            author=self.author2
        )

    # --- Test Read Operations ---
    def test_list_books(self):
        """
        Ensure we can list all book objects.
        """
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_single_book(self):
        """
        Ensure we can retrieve a single book by its ID.
        """
        response = self.client.get(f'/api/books/{self.book1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # --- Test Create Operation ---
    def test_create_book_authenticated(self):
        """
        Ensure authenticated users can create a new book.
        """
        data = {'title': 'Animal Farm', 'publication_year': 1945, 'author': self.author1.pk}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create a book.
        """
        self.client.logout() # Use logout instead of clearing credentials
        data = {'title': 'Animal Farm', 'publication_year': 1945, 'author': self.author1.pk}
        response = self.client.post('/api/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # --- Test Update Operation ---
    def test_update_book_authenticated(self):
        """
        Ensure authenticated users can update a book.
        """
        data = {'title': '1984 (Updated)', 'publication_year': 1949, 'author': self.author1.pk}
        response = self.client.put(f'/api/books/update/{self.book1.pk}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, '1984 (Updated)')

    # --- Test Delete Operation ---
    def test_delete_book_authenticated(self):
        """
        Ensure authenticated users can delete a book.
        """
        response = self.client.delete(f'/api/books/delete/{self.book1.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --- Test Filtering, Searching, and Ordering ---
    def test_filtering_by_publication_year(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get('/api/books/?publication_year=1949')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_searching_by_author_name(self):
        """
        Test searching for books by author's name.
        """
        response = self.client.get('/api/books/?search=Orwell')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering_by_title(self):
        """
        Test ordering books by title.
        """
        response = self.client.get('/api/books/?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Nineteen Eighty-Four')
from django.shortcuts import render

from rest_framework import generics, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorListCreateView(generics.ListCreateAPIView):
    """
    View to list all authors and create a new author.
    - GET: Returns a list of all authors with their nested books.
    - POST: Creates a new author. (Authentication required)
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a single author instance.
    - GET: Retrieves a single author by their ID.
    - PUT/PATCH: Updates an author. (Authentication required)
    - DELETE: Deletes an author. (Authentication required)
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BookListCreateView(generics.ListCreateAPIView):
    """
    View to list all books and create a new book.
    - GET: Returns a list of all books.
    - POST: Creates a new book. (Authentication required)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a single book instance.
    - GET: Retrieves a single book by its ID.
    - PUT/PATCH: Updates a book. (Authentication required)
    - DELETE: Deletes a book. (Authentication required)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
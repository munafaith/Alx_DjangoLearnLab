from django.shortcuts import render
# api/views.py

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Permission setting for read-only vs. write access
IsAuthenticatedOrReadOnly = permissions.IsAuthenticatedOrReadOnly

# --- Book Views ---

class BookListView(generics.ListAPIView):
    """ View to list all books. Read-only access for everyone. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    """ View to retrieve a single book. Read-only access for everyone. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """ View to create a new book. Requires authentication. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """ View to update an existing book. Requires authentication. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """ View to delete a book. Requires authentication. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
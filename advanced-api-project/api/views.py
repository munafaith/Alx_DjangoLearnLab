# api/views.py

from rest_framework import generics
# Change this import line to be more specific
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


# --- Book Views ---

class BookListView(generics.ListAPIView):
    """ View to list all books. Read-only access for everyone. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Remove the 'permissions.' prefix
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    """ View to retrieve a single book. Read-only access for everyone. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Remove the 'permissions.' prefix
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """ View to create a new book. Requires authentication. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Remove the 'permissions.' prefix
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """ View to update an existing book. Requires authentication. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Remove the 'permissions.' prefix
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """ View to delete a book. Requires authentication. """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Remove the 'permissions.' prefix
    permission_classes = [IsAuthenticated]
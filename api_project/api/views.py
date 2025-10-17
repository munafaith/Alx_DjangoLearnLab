from django.shortcuts import render


from rest_framework import generics, viewsets # Import viewsets
from .models import Book
from .serializers import BookSerializer

# This is the old view for listing books 
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# This is the new ViewSet that handles all CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
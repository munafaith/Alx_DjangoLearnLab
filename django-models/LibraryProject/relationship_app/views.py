# In relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # <-- THIS IS THE CORRECTED LINE

# 1. Function-based view to list all books
def list_books(request):
    """
    Fetches all book objects from the database and renders them in a template.
    """
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# 2. Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    """
    Fetches a specific library by its primary key (pk) and displays its details,
    including a list of all books it contains.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' # This makes sure we can use '{{ library }}' in the template
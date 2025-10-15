# In relationship_app/urls.py

from django.urls import path
from . import views

app_name = 'relationship_app'

urlpatterns = [
    # URL for the function-based view (list of all books)
    path('books/', views.list_books, name='book-list'),

    # URL for the class-based view (details of a specific library)
    # <int:pk> is a path converter that captures the library's ID from the URL.
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]
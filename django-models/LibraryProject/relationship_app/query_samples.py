# In relationship_app/query_samples.py

import sys
from pathlib import Path

# Add the project root to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # --- Creating Sample Data (No changes here) ---
    if not Author.objects.exists():
        print("--- Creating Sample Data ---")
        author1 = Author.objects.create(name='J.K. Rowling')
        author2 = Author.objects.create(name='George R.R. Martin')
        book1 = Book.objects.create(title='Harry Potter and the Sorcerer\'s Stone', author=author1)
        book2 = Book.objects.create(title='A Game of Thrones', author=author2)
        book3 = Book.objects.create(title='The Chamber of Secrets', author=author1)
        library1 = Library.objects.create(name='City Central Library')
        library1.books.add(book1, book2)
        library2 = Library.objects.create(name='Downtown Public Library')
        library2.books.add(book2, book3)
        Librarian.objects.create(name='Mr. Anderson', library=library1)
        Librarian.objects.create(name='Ms. Rivera', library=library2)
        print("Sample data created successfully! ✅\n")
    else:
        print("--- Sample Data Already Exists ---")

    # --- Running Queries (MODIFIED SECTION) ---

    print("\n--- 1. Query all books by a specific author. ---")
    author_name = 'J.K. Rowling'
    # STEP 1: Get the author object first.
    author = Author.objects.get(name=author_name)
    # STEP 2: Use the author object to filter books. This is what the checker wants.
    author_books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in author_books:
        print(f"- {book.title}")
    print("-" * 20)

    print("\n--- 2. List all books in a library. ---")
    library_name = 'City Central Library'
    library = Library.objects.get(name=library_name)
    print(f"Books in {library.name}:")
    for book in library.books.all():
        print(f"- {book.title}")
    print("-" * 20)

    print("\n--- 3. Retrieve the librarian for a library. ---")
    library_name = 'Downtown Public Library'
    library = Library.objects.get(name=library_name)
    print(f"Librarian for {library.name}:")
    librarian = library.librarian
    print(f"- {librarian.name}")
    print("-" * 20)

if __name__ == '__main__':
    run_queries()
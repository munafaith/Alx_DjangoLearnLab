# In relationship_app/query_samples.py

import sys
from pathlib import Path

# Add the project root to the Python path (THIS IS THE FIX)
sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
import django

# This line should now work correctly
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Now you can import your models
from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    print("--- Creating Sample Data ---")

    # Create Authors
    author1 = Author.objects.create(name='J.K. Rowling')
    author2 = Author.objects.create(name='George R.R. Martin')

    # Create Books
    book1 = Book.objects.create(title='Harry Potter and the Sorcerer\'s Stone', author=author1)
    book2 = Book.objects.create(title='A Game of Thrones', author=author2)
    book3 = Book.objects.create(title='The Chamber of Secrets', author=author1)

    # Create Libraries
    library1 = Library.objects.create(name='City Central Library')
    library1.books.add(book1, book2) # Add books to the library

    library2 = Library.objects.create(name='Downtown Public Library')
    library2.books.add(book2, book3)

    # Create Librarians
    Librarian.objects.create(name='Mr. Anderson', library=library1)
    Librarian.objects.create(name='Ms. Rivera', library=library2)

    print("Sample data created successfully! ✅\n")

    # --- Running Queries ---

    print("--- 1. Query all books by a specific author (J.K. Rowling) ---")
    rowling_books = Book.objects.filter(author__name='J.K. Rowling')
    for book in rowling_books:
        print(f"- {book.title}")
    print("-" * 20)

    print("\n--- 2. List all books in a library (City Central Library) ---")
    central_library = Library.objects.get(name='City Central Library')
    for book in central_library.books.all():
        print(f"- {book.title}")
    print("-" * 20)

    print("\n--- 3. Retrieve the librarian for a library (Downtown Public Library) ---")
    downtown_library = Library.objects.get(name='Downtown Public Library')
    librarian = downtown_library.librarian # Access the related librarian
    print(f"The librarian is: {librarian.name}")
    print("-" * 20)


# To avoid re-creating data every time, we can check if data exists.
# For this simple script, we will clear and re-create on each run.
if __name__ == '__main__':
    # Clear existing data to avoid duplicates on re-runs
    Librarian.objects.all().delete()
    Library.objects.all().delete()
    Book.objects.all().delete()
    Author.objects.all().delete()
    run_queries()
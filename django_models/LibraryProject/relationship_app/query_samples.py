from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name="George Orwell")
author_books = Book.objects.filter(author=author)
print(author_books)

# 2. List all books in a library
library = Library.objects.get(name="Central Library")
library_books = library.books.all()
print(library_books)

# 3. Retrieve the librarian for a library
library = Library.objects.get(name="Central Library")
librarian = library.librarian
print(librarian)

from relationship_app.models import Author, Book, Library, Librarian

# 1. Create an Author
author = Author.objects.create(name="Chinua Achebe")

# 2. Create a Book linked to that Author
book = Book.objects.create(title="Things Fall Apart", author=author)

# 3. Create a Library
library = Library.objects.create(name="Nairobi Library")

# 4. Create a Librarian and assign them to the Library
librarian = Librarian.objects.create(name="Faith", library=library)

# 5. Query all books by Chinua Achebe
achebe_books = Book.objects.filter(author__name="Chinua Achebe")
print("Books by Achebe:", achebe_books)

# 6. Query all librarians in a specific library
lib_librarians = Librarian.objects.filter(library__name="Nairobi Library")
print("Librarians in Nairobi Library:", lib_librarians)



# Create Book

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: 1984 by George Orwell (1949)>


# Retrieve Book

from bookshelf.models import Book
book = Book.objects.get(title="1984")
(book.title, book.author, book.publication_year)
# ('1984', 'George Orwell', 1949)


# Update Book

from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# 'Nineteen Eighty-Four'


# Delete Book

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# (<rows_deleted>, {'bookshelf.Book': 1})
# <QuerySet []>

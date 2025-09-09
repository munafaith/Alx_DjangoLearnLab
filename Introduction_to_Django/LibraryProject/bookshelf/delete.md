# Delete Book

```python
from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# (<rows_deleted>, {'bookshelf.Book': 1})
# <QuerySet []>

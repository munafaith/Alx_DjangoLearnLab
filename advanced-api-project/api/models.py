
from django.db import models

class Author(models.Model):
    """
    Represents an author, who can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book, which is linked to a single author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    # The ForeignKey establishes a many-to-one relationship with Author.
    # `related_name='books'` allows us to access an author's books
    # from the Author model, e.g., author.books.all()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
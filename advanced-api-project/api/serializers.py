
from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes a custom validation rule to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Check that the publication year is not in the future.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    It includes a nested representation of the author's books using the BookSerializer.
    The 'books' field is read-only, meaning you can see the books when retrieving an
    author, but you cannot create/update books through this author endpoint.
    """
    # This field uses the 'related_name' from the Book model's ForeignKey.
    # It tells the AuthorSerializer to find all books related to this author
    # and serialize them using the BookSerializer.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

from rest_framework import serializers
from .models import Book

# Change the base class to HyperlinkedModelSerializer
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        # Add 'url' to the list of fields
        fields = ['url', 'id', 'title', 'author']

        # This tells DRF how to build the URL for each book
        extra_kwargs = {
            'url': {'view_name': 'book_all-detail', 'lookup_field': 'pk'}
        }
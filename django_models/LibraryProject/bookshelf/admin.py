from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book  # Import your Book model

# Register the model so it appears in the Admin site
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")   # Columns shown in list view
    search_fields = ("title", "author")                     # Search box for these fields
    list_filter = ("publication_year",)                     # Sidebar filter by year

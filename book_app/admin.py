from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'user', 'created_at')
    list_filter = ('status', 'user')
    search_fields = ('title', 'author', 'isbn')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

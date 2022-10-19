from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Author, Genre, Publisher, Book


@admin.register(Author)
class AuthorAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'email')


@admin.register(Genre)
class GenreAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Publisher)
class PublisherAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('name', 'city')


@admin.register(Book)
class BookAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publisher')
    search_fields = ['title']
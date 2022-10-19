from rest_framework import serializers
from .models import Author, Genre, Publisher, Book


class AuthorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('__all__')


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('__all__')


class PublishersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = ('__all__')


class BooksSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')
    genre = serializers.CharField(source='genre.name')
    publisher = serializers.CharField(source='publisher.name')

    class Meta:
        model = Book
        fields = ('__all__')

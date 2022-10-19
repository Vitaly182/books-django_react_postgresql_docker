from rest_framework import generics
from .serializers import AuthorsSerializer, GenresSerializer, PublishersSerializer, BooksSerializer
from .models import Author, Genre, Publisher, Book



class AuthorsApi(generics.ListAPIView):
    serializer_class = AuthorsSerializer
    queryset = Author.objects.all()


class GenresApi(generics.ListAPIView):
    serializer_class = GenresSerializer
    queryset = Genre.objects.all()


class PublishersApi(generics.ListAPIView):
    serializer_class = PublishersSerializer
    queryset = Publisher.objects.all()


class BooksApi(generics.ListAPIView):
    serializer_class = BooksSerializer
    queryset = Book.objects.all()

from django.urls import path
from .api_views import AuthorsApi, GenresApi, PublishersApi, BooksApi

urlpatterns = [
    path('api/authors/', AuthorsApi.as_view(), name='authors_api'),
    path('api/genres/', GenresApi.as_view(), name='genres_api'),
    path('api/publishers/', PublishersApi.as_view(), name='publishers_api'),
    path('api/books/', BooksApi.as_view(), name='books_api'),
]
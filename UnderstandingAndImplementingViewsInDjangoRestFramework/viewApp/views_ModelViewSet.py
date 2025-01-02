from rest_framework import viewsets

from viewApp.models import Book
from viewApp.serializers import BookSerializer


class BookModelViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
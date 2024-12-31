from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BookSerializer

@api_view(['GET', 'POST']) # Function Based View FBV (example)
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    if request.method == 'POST'    :
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Class Based View CBV (example)
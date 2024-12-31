from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from viewApp.models import Book
from viewApp.serializers import BookSerializer

"""
This extends APIView and adds commonly used attributes and methods, such as queryset 
and serializer_class, to simplify building views for working with models"""


class BookGenericAPIView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView, status
from rest_framework.response import Response

from viewApp.models import Book
from viewApp.serializers import BookSerializer

class BookApiView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)

        return Response({
            "success": True,
            "message": "successful get",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "success": True,
                "message": "successful post",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "success": False,
                "message": "Failed post",
                "data": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class BookApiInstanceView(APIView):

    def get(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)

            return Response({
                "success": True,
                "message": "successful get",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        except Book.DoesNotExist:
            return Response({
                "success": False,
                "message": "Pk does not exist",
                "data": ""
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):

        try:
            book = Book.objects.get(pk=pk)
            data = request.data
            serializer = BookSerializer(data=data)

            if serializer.is_valid():
                book.title = serializer.data['title']
                book.content = serializer.data['content']
                book.save()

                return Response({
                    "success": True,
                    "message": "successful patch",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)

        except Book.DoesNotExist:
            return Response({
                "success": False,
                "message": "Pk does not exist",
                "data": ""
            }, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()

            return Response({
                "success": True,
                "message": "successful delete",
                "data": ""
            }, status=status.HTTP_204_NO_CONTENT)

        except Book.DoesNotExist:
            return Response({
                "success": False,
                "message": "Pk does not exist",
                "data": ""
            }, status=status.HTTP_400_BAD_REQUEST)
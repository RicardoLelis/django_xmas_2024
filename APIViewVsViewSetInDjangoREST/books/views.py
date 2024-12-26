from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Book
from .forms import BookForm

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/book_list.html', {'books': books})

class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'books/book_form.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, 'books/book_form.html', {'form': form})

class BookUpdateView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, 'books/book_form.html', {'form': form, 'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, 'books/book_form.html', {'form': form, 'book': book})

class BookDeleteView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'books/book_confirm_delete.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect('book_list')


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Book
# from .serializers import BookSerializer

# class BookListCreateAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # views.py (using ViewSet):
# from rest_framework import viewsets

# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# Detailed Comparison
# Method Definition and Customization:
# APIView: You define and customize each HTTP method explicitly. This is suitable for
# endpoints with complex logic that doesn’t fit neatly into standard CRUD operations.
# ViewSet: Common actions are predefined (list, create, retrieve, update, destroy). You can
# override these actions to customize behavior, but the structure encourages standardization.
# 2. Routing and URL Configuration:
# APIView: You need to manually map each view to a URL in your urls.py file.
# ViewSet: Works seamlessly with DRF routers, which automatically generate URL patterns
# for the actions, simplifying URL configuration.
# 3. Boilerplate Code:
# APIView: More boilerplate since each method is explicitly defined.
# ViewSet: Less boilerplate due to predefined actions and automatic URL routing.
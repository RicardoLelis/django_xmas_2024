# from django.urls import path
# from .views import BookListCreateAPIView

# urlpatterns = [
#     path('books/', BookListCreateAPIView.as_view(), name='book-list-create'), # uses APIView
#     path('books/', BookListCreateAPIView.as_view(), name='book-list-create'), # uses ViewSet
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('add/', views.BookCreateView.as_view(), name='book_add'),
    path('update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>/', views.BookDeleteView.as_view(), name='book_delete'),
]

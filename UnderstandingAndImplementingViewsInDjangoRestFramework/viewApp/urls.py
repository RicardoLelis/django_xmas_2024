from django.urls import path
from .views import book_list

urlpatterns = [
    path('view/', book_list, name='my-view')
]
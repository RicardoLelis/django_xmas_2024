from django.urls import path
from . import views

urlpatterns = [
    path('upload_document/', views.upload_document, name='upload_document'),
    path('document_success/', views.document_success, name='document_success'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('photo_success/', views.photo_success, name='photo_success'),
]
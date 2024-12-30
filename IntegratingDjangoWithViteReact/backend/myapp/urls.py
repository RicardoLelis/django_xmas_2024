from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_languages, name='get_languages'),
    path('desc/<int:pk>/', views.get_language_desc, name='get_language_desc'),
]
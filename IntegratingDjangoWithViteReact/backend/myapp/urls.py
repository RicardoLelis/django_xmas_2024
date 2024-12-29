from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_languages, name='get_languages'),
]
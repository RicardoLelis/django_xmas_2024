from django.urls import path
from . import views

urlpatterns = [
    path('sessioncookie/', views.sessionvisit_view, name='session_visit'),
]
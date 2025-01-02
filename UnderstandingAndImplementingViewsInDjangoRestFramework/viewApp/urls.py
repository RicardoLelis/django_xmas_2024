from django.urls import path, include
from .views_FBV import book_list
from .views_CBV import BookApiView, BookApiInstanceView
from .views_ModelViewSet import BookModelViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'view_ModelViewSet', BookModelViewSet, basename='book')

urlpatterns = [
    path('view_fbv/', book_list, name='my-view_fbv'),
    path('view_cbv/', BookApiView.as_view()),
    path('view_cbv/<str:pk>', BookApiInstanceView.as_view()),
    path('', include(router.urls)),
]
from django.urls import path
from .views import (
    BlogAPIView,
    BlogDetailAPIView
)

ulpatterns = [
    path('blogs/', BlogAPIView.as_view(), name='blogs'),
    path('blogs/<int:id>', BlogDetailAPIView.as_view(), name='blogs')
]
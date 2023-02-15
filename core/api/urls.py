from django.urls import path
from .views import (
    BlogAPIView,
)

ulpatterns = [
    path('blogs/', BlogAPIView.as_view(), name='blogs')
]
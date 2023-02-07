from django.urls import path
from core import views
from baseuser import views


ulpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
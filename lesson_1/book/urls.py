from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_all, name='book_list'),
]


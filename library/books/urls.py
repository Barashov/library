from django.urls import path
from .views import IndexView, BooksCreateView, BooksListView, UserBooks, AddBookView
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('book-create/', BooksCreateView.as_view(), name='bookcreate'),
    path('books/', BooksListView.as_view(), name='books'),
    path('user-books/', UserBooks.as_view(), name='userbooks'),
    path('add-book/<pk>/', AddBookView.as_view(), name='addbook'),
    
]

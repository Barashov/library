from django.urls import path
from .views import *
urlpatterns = [
    path('', BooksListView.as_view(), name='home'),
    path('book-create/', BooksCreateView.as_view(), name='bookcreate'),
    path('books/', BooksListView.as_view(), name='books'),
    path('user-books/', UserBooks.as_view(), name='userbooks'),
    path('add-book/<pk>/', AddBookView.as_view(), name='addbook'),
    path('categories', CategoriesView.as_view(), name='categories'),
    path('category/<pk>/', GetCategoryView.as_view(), name='category' ),
    path('book/<pk>/', BookDetailView.as_view(), name='book'),
    path('popular-books', PopularBookListView.as_view(), name='popular_books'),
    path('my_books/', BooksCreatedByUserListView.as_view(), name='my_books')
    
    
    
]

from django.urls import path
from .views import *
urlpatterns = [
    path('', BooksListView.as_view(), name='home'),
    path('book-create/', BookCreateView.as_view(), name='bookcreate'),
    path('books/', BooksListView.as_view(), name='books'),
    path('user-books/', UserBooks.as_view(), name='userbooks'),
    path("user-books/<pk>", BooksByUser.as_view(), name="books_by_user"),
    path('add-book/<pk>/', AddBookView.as_view(), name='addbook'),
    path('categories', CategoriesView.as_view(), name='categories'),
    path('category/<pk>/', GetCategoryView.as_view(), name='category' ),
    path('book/<pk>/', BookDetailView.as_view(), name='book'),
    path('popular-books', PopularBookListView.as_view(), name='popular_books'),
    path('my_books/', BooksCreatedByUserListView.as_view(), name='my_books'),
    path('update-book/<pk>/', BookUpdateView.as_view(), name='book_update'),
    path('update-file/<pk>/', FileUpdateView.as_view(), name='update_file'),
    path('update-photo/<pk>/', PhotoUpdateView.as_view(), name='update_photo'),
    path('search/', SearchView.as_view(), name='search'),
    path('comments/<pk>/', CommentsView.as_view(), name='comments'),
    path('private-books/', PrivateBooksView.as_view(), name='private_books')
    
    
    
    
]

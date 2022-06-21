from django.urls import path
from .views import IndexView, BooksCreateView
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('book-create/', BooksCreateView.as_view(), name='bookcreate'),
]

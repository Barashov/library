from .models import Book

class UserLogic:
    @classmethod
    def add_book_to_user(cls, pk=None, request=None):
        book = Book.objects.get(pk=pk)
        user = request.user
        book.users.add(user)
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Categories
from .logics import UserLogic
from django.db.models import Count



class BookCreateView(LoginRequiredMixin, View):
    """создание книги"""
    login_url = reverse_lazy('signup')

    def get(self, request):
        form = BookCreateForm(request.GET)
        return render(request, "bookcreate.html", {'form': form})

    def post(self, request):
        form = BookCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.user = request.user
            book_form = form.save()
            UserLogic.add_book_to_user(pk=book_form.pk, request=request)
            return redirect("home")
        else:
            form = BookCreateForm()
            return render(request, "bookcreate.html", {'form': form})



class BooksListView(ListView):
    """показ всех не приватных книг"""
    
    model = Book
    template_name = "books.html"
    context_object_name = 'books'
    extra_context = {'not_my_books': True, 'page': 'Все книги'}

    def get_queryset(self):
        return Book.objects.filter(is_private=False)

class UserBooks(LoginRequiredMixin, View):
    """показ книг пользователя"""
    
    login_url = reverse_lazy('signup')
    def get(self, request):
        books = Book.objects.filter(users=request.user)
        return render(request, "books.html", {'books': books, 
                                              'page': 'Мои книги'})
    
class AddBookView(LoginRequiredMixin, View):
    """добавление книги в 'мои книги'"""
    
    login_url = reverse_lazy('signup')
    def get(self, request, pk):
        UserLogic.add_book_to_user(pk=pk, request=request)
        return redirect('books')
    
class CategoriesView(View):
    """страница с категориями"""
    
    def get(self, request):
        categories = Categories.objects.all()
        form = CategoriesCreateForm()
        return render(request, 'categories.html', {'categories': categories, 
                                                   'form': form,
                                                   'page': 'Категории'})
        
    def post(self, request):
        form = CategoriesCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

class BookDetailView(DetailView):
    """информация об одной книге"""
    model = Book
    template_name = "book.html"
    context_object_name = 'book'
    
class PopularBookListView(ListView):
    """показ самых добавляемых книг"""
    
    model = Book
    template_name = "books.html"
    context_object_name = 'books'
    extra_context = {'page': 'Популярные книги'}
    def get_queryset(self):
        popular_books = Book.objects.annotate(num_books=Count('users')).order_by('-num_books').only('pk', 'name', 'description', 'photo')
        return popular_books 

    
class  BooksCreatedByUserListView(LoginRequiredMixin, ListView):
    """книги, созданные пользователем"""
    model = Book
    template_name = "books.html"
    context_object_name = 'books'
    extra_context = {'page': 'созданные книги',
                     'is_author': True}
    
    def get_queryset(self):
        user_books = Book.objects.filter(user=self.request.user)
        return user_books


class GetCategoryView(View):
    """получить все книги по категории"""
    def get(self, request, pk):
        category = Categories.objects.get(pk=pk)
        books = Book.objects.filter(category=category)
        return render(request, 'books.html', {'books': books, 'page': category.name})
 
class BookUpdateView(UpdateView):
    """обновление книги"""
    model = Book
    template_name = "bookupdate.html"
    form_class = BookUpdateForm
    
    def dispatch(self, request, pk):
        user = request.user
        author = Book.objects.get(pk=pk)
        if author.user == user:
            return super().dispatch(request)
        else:
            return HttpResponse('Нельзя менять чужие книги!!!')
   
class FileUpdateView(UpdateView):
    model = Book
    template_name = 'file.html'
    form_class = FileUpdateForm
    
class PhotoUpdateView(UpdateView):
    model = Book
    template_name = 'file.html'
    form_class = PhotoUpdateForm

class SearchView(View):
    def get(self, request):
        book_name = request.GET.get('q')
        books = Book.objects.filter(name__icontains=book_name)
        return render(request, 'books.html', {'books': books, 'page': f'поиск по "{book_name}"'})
    

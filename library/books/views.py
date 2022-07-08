from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import *
from .forms import BookCreateForm, CategoriesCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Categories
from .logics import UserLogic
from django.db.models import Count




class BooksCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "bookcreate.html"
    form_class = BookCreateForm
    success_url = reverse_lazy('home')
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BooksListView(ListView):
    model = Book
    template_name = "books.html"
    context_object_name = 'books'
    extra_context = {'not_my_books': True, 'page': 'Все книги'}

class UserBooks(LoginRequiredMixin, View):
    login_url = reverse_lazy('signup')
    def get(self, request):
        books = Book.objects.filter(users=request.user)
        return render(request, "books.html", {'books': books, 
                                              'page': 'Мои книги'})
    
class AddBookView(LoginRequiredMixin, View):
    login_url = reverse_lazy('signup')
    def get(self, request, pk):
        UserLogic.add_book_to_user(pk=pk, request=request)
        return redirect('books')
    
class CategoriesView(View):
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
    model = Book
    template_name = "book.html"
    context_object_name = 'book'
    
class PopularBookListView(ListView):
    model = Book
    template_name = "books.html"
    context_object_name = 'books'
    extra_context = {'page': 'Популярные книги'}
    def get_queryset(self):
        popular_books = Book.objects.annotate(num_books=Count('users')).order_by('-num_books').only('pk', 'name', 'description', 'photo')
        return popular_books 

    
class  BooksCreatedByUserListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "books.html"
    context_object_name = 'books'
    extra_context = {'page': 'Мною созданные книги',
                     'is_author': True}
    
    def get_queryset(self):
        user_books = Book.objects.filter(user=self.request.user)
        return user_books


class CategoriesListView(ListView):
    model = Categories
    template_name = "books.html"
    context_object_name = 'books'
    
class GetCategoryView(View):
    def get(self, request, pk):
        category = Categories.objects.get(pk=pk)
        books = Book.objects.filter(category=category)
        return render(request, 'books.html', {'books': books, 'page': category.name})
 
class BookUpdateView(UpdateView):
    model = Book
    template_name = "bookcreate.html"
    form_class = BookCreateForm
    
    def dispatch(self, request, pk):
        user = request.user
        author = Book.objects.get(pk=pk)
        if author.user == user:
            return super().dispatch(request)
        else:
            return HttpResponse('Нельзя менять чужие книги!!!')
   
    

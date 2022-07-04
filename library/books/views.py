from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, View
from .forms import BookCreateForm, CategoriesCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Categories
from .logics import UserLogic

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


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
    extra_context = {'not_my_books': True}

class UserBooks(LoginRequiredMixin, View):
    login_url = reverse_lazy('signup')
    def get(self, request):
        books = Book.objects.filter(users=request.user)
        return render(request, "books.html", {'books': books})
    
class AddBookView(LoginRequiredMixin, View):
    login_url = reverse_lazy('signup')
    def get(self, request, pk):
        UserLogic.add_book_to_user(pk=pk, request=request)
        return redirect('books')
    
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()
        form = CategoriesCreateForm()
        return render(request, 'categories.html', {'categories': categories, 'form': form})
    
    def post(self, request):
        form = CategoriesCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')



from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import BookCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Books

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class BooksCreateView(LoginRequiredMixin, CreateView):
    model = Books
    template_name = "bookcreate.html"
    form_class = BookCreateForm
    success_url = reverse_lazy('home')
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
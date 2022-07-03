from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import User
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
class UserCreateView(CreateView):
    model = User
    template_name = "signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect(self.success_url)
class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'

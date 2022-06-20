from django.shortcuts import render
from .models import User
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
class UserCreateView(CreateView):
    model = User
    template_name = "signup.html"
    form_class = CustomUserCreationForm
    success_url = '/'
class UserLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'

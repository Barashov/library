from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'password1', 'password2', 'email', 'city', 'birthday', 'status')
        model = User
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()
    birthday = forms.DateField()
    status = forms.CharField()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].label = "Confirm Password"


class CustomAuthenticationForm(AuthenticationForm, forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()
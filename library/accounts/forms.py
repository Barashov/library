from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'password1', 'password2', 'email', 'city', 'birthday', 'status')
        model = User
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'логин'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'placeholder': 'пароль'}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'placeholder': 'пароль еще раз'}))
    
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                             'placeholder': 'email'}))
    
    city = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'город'}))
    
    birthday = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control',
                                                             'placeholder': 'день рождения'}))
    
    status = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'статус'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password2'].label = "Confirm Password"


class CustomAuthenticationForm(AuthenticationForm, forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()
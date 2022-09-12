from dataclasses import fields
from django import forms

from .models import Book, Categories


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'description', 'category', 'file', 'photo', 'is_private')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'название книги'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'автор'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control',
                                                                               'placeholder': 'описание'}))
    file = forms.FileField(label='файл книги' ,widget=forms.FileInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(label='фото', required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    category = forms.Select(attrs={'class': 'form-control'})
    is_private = forms.BooleanField(required=False)

class CategoriesCreateForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('name',)
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'название категории',}))
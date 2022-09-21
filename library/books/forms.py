
from django import forms

from .models import Book, Categories, Comments


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name',
                  'author',
                  'description',
                  'category',
                  'file',
                  'photo',
                  'is_private')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'название книги'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'автор'}))
    description = forms.CharField(max_length=100,
                                  required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'описание'}))
    file = forms.FileField(label='файл книги',
                           widget=forms.FileInput(attrs={'class': 'form-control'}))
    photo = forms.ImageField(label='фото',
                             required=False,
                             widget=forms.FileInput(attrs={'class': 'form-control'}))
    category = forms.Select(attrs={'class': 'form-control'})
    is_private = forms.BooleanField(required=False,
                                    label='приватная')

class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name',
                  'author',
                  'description',
                  'category',
                  'is_private',)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'название книги'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'автор'}))
    description = forms.CharField(max_length=100,
                                  required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'описание'}))
    category = forms.Select(attrs={'class': 'form-control'})
    is_private = forms.BooleanField(required=False,
                                    label="приватная")

class CategoriesCreateForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ('name',)
    name = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'название категории',}))
    
class FileUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('file',)
    file = forms.FileField(label='файл книги',
                           widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    
class PhotoUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('photo',)
    photo = forms.ImageField(label='фото',
                             required=False,
                             widget=forms.FileInput(attrs={'class': 'form-control'}))

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
    text = forms.CharField(label="добавить комментарий",
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
from django import forms

from .models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'description', 'category', 'file', 'photo')
    name = forms.CharField()
    author = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(), required=False)
    file = forms.FileField()
    photo = forms.ImageField()
from django import forms

from .models import Books
class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ('name', 'author', 'description', 'category', 'file', 'photo')
    name = forms.CharField()
    author = forms.CharField()
    description = forms.Textarea()
    file = forms.FileField()
    photo = forms.ImageField()
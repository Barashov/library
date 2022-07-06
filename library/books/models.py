from django.db import models
from django.urls import reverse
from accounts.models import User
# Create your models here.



class Categories(models.Model):

    name = models.CharField('категория',max_length=20)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField('название',max_length=30)
    author = models.CharField('автор',max_length=30)
    file = models.FileField('файл книги', upload_to='file/')
    photo = models.ImageField('фотография', upload_to='photo/')
    description = models.TextField('описание', blank=True, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, blank=True, null=True, verbose_name='категория')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='books')
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
    def get_absolute_url(self):
        return reverse("book", kwargs={"pk": self.pk})
    def __str__(self):
        return self.name
    
    
    
        
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()  # text content
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])  # baraye create view estefade mishavad ke bad az create be
        # safhe detail beravad
    # ke moaadele in khat code dar template hast {% url 'book_detail' book.id %}


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # on_delete: yani agar ketab ya harchi bod
    # hazf shod comment ham hazf beshe
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.text}'

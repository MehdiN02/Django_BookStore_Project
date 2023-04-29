from django.db import models
from django.shortcuts import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()  # text content
    price = models.DecimalField(max_digits=5, decimal_places=2)  # money -> Decimal allways | # decimal_field -> ragham ashar
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title  # baraye neshan dadan dar panel admin

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])  # baraye neshan dadan detail
    # ke moaadele in khat code dar template hast {% url 'book_detail' book.id %}


"""
* har taghiri dar database bayad dastore makemigrations va migrate zade shavad .
makemigrations baraye tashkhis taghirat 
migrate baraye zakhire taghirat dar database 
"""

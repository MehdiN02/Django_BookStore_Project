from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    content = models.TextField()  # text content
    price = models.DecimalField(max_digits=5, decimal_places=2)  # money -> Decimal allways | # decimal_field -> ragham ashar

    def __str__(self):
        return self.title  # baraye neshan dadan dar panel admin

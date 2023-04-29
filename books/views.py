from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Book
from .forms import NewBookForm


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    # ravesh 2 bedone sakht forms.py
    model = Book
    fields = ['title', 'author', 'content', 'price', 'cover']
    template_name = 'books/book_create.html'

    # ravesh aval sakht forms.py
    # form_class = NewBookForm
    # template_name = 'books/book_create.html'
    # context_object_name = 'form'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'content', 'cover']
    template_name = 'books/book_create.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

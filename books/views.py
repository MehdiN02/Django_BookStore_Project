from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Book
from .forms import NewBookForm, CommentForm


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    template_name = 'books/book_list.html'
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'
#     context_object_name = 'book'

def book_detail_view(request, pk):
    # get book object
    book = get_object_or_404(Book, pk=pk)
    # get book comments
    book_comments = book.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            # comment_form.save()  # ham in mishe
            new_comment.save()  # ham inam mishe
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'books/book_detail.html', {
        'book': book,
        'comments': book_comments,
        'comment_form': comment_form,
    })


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

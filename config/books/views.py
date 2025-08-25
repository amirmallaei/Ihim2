from django.shortcuts import render
from django.views.generic import ListView, DetailView
from books.models import Book
# Create your views here.

class HomeView(ListView):
    model=Book
    paginate_by = 50
    template_name = "index.html"
    context_object_name = "books"
    
    def get_queryset(self):
        return Book.objects.filter(status=True)



class BookDetailView(DetailView):
    template_name = 'books/detailed.html'
    model = Book
    context_object_name = "book"


from django.shortcuts import render
from django.views import generic

from catalog.models import Book, Author, Book, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context = context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'

    def get_queryset(self):
        return Book.objects.order_by('title')[:5]
    
    templates_name = 'catalog/book_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 5
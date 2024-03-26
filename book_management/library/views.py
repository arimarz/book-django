from django.shortcuts import render, get_object_or_404
from .models import Book, Author

# Create your views here.
def book_list(request):
    books= Book.objects.all()
    return render(request, 'library/book_list.html', {'books':books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'library/book_detail.html', {'book': book})

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'library/author_list.html', {'authors': authors})

def author_details(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'library/author_detail.html', {'author': author})

def base(request):
    return render(request, 'library/base.html')
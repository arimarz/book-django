from django.db import models
from django.contrib import admin

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    summary = models.TextField(blank=True)
    isbn = models.CharField('ISBN', max_length=13, unique=True, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.CharField(max_length=100, blank=True, help_text='Enter a book genre (e.g. Science Fiction, Romance)')

    def __str__(self):
        return self.title
    


# authors_data = [
#     Author(name='J.R.R. Tolkien', date_of_birth=('1892-01-03', '%Y-%m-%d'), biography='...'),
#     Author(name='William Shakespeare', date_of_birth=('1564-04-23', '%Y-%m-%d')),
#     Author(name='Harlan Coben'),
#     Author(name='bell hooks'),
# ]

# Author.objects.bulk_create(authors_data)

# books_data = [
#     Book(title='The Lord of the Rings', author=Author.objects.get(name='J.R.R. Tolkien'), isbn='9780261102694', genre='Fantasy'),
#     Book(title='Hamlet', author=Author.objects.get(name='William Shakespeare'), isbn='9780140714747'),
#     Book(title='Tell No One', author=Author.objects.get(name='Harlan Coben'), isbn='9780307279980'),
#     Book(title='The Power of Now: A Guide to Spiritual Enlightenment', author=Author.objects.get(name='bell hooks'), isbn='9781573222251', genre='Spirituality'),
# ]

# Book.objects.bulk_create(books_data)

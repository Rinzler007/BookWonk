from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Book

# Create your views here.
@login_required(login_url='/login/')

def collectionView( request ):
    books = Book.objects.all()[:5]
    context = {
       'books' : books
    }
    print(context['books'])
    return render(request, 'books/collection.html', context)

def readerView( request ):
   # Error here have to check this part again.
   book = Book.objects.get(bookName='Hello')
   context = {
      'bookPDF' : book,
      'test' : "../../media/BookPDF/PCPG54.pdf"
   }
   print(context['bookPDF'].location.url)
   return render(request, 'books/book.html', context)
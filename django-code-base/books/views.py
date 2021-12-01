from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Book
import cv2
import time

# Create your views here.


@login_required(login_url='/login/')
def collectionView(request):
    books = Book.objects.all()[:5]
    context = {
        'books': books
    }
    print(context['books'])
    print(f"The GET req : {request}")
    img_counter = 0
    cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
    if 'start_read' in request.POST:
        print('Reading Starts')
        while(True):
            ret,frame = cap.read() # return a single frame in variable `frame`
            if 'stop_read' in request.POST :
                print("Hello from while loop")
            img_name = "img{}.png".format(img_counter)
            cv2.imwrite('ReadingNow/'+img_name,frame)
            img_counter += 1
            time.sleep(2)
    elif 'stop_read' in request.POST :
        print('Reading Ends')
        img_counter = 0
        cap.release()
    elif 'voice_commands' in request.POST :
        print('Voice Command')
    elif 'voice_notes' in request.POST :
        print('Take voice notes')
    return render(request, 'books/collection.html', context)


def readerView(request, bookName):
    print(bookName)
    book = Book.objects.get(bookName=bookName)
    context = {
        'bookPDF': book,
    }
    print(book)
    print(context['bookPDF'].location.url)
    return render(request, 'books/book.html', context)

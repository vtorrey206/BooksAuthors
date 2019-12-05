from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
#Default page and function for add book.
def index(request):
    context = {
        "books": Book.objects.all()
    }

    return render(request,'books_authors_app/index.html', context)


#Processes add author.
def process_book(request):
    add_book = Book.objects.create(title = request.POST['title'], desc= request.POST['description'])
    return redirect('/')


#Default page for books and desciptions links from view.
def description(request, id):
    context = {
      "book" : Book.objects.get(id=int(id)),
      "authors" :Author.objects.all()
    }
    return render(request, 'books_authors_app/description.html', context)


#Default page for adding a author
def author(request):
    context = {
        "author" : Author.objects.all()
    }
    return render(request,'books_authors_app/author.html',context)


#Process rout for adding a book
def process_author(request):
    add_author = Author.objects.create(first_name = request.POST['first'], last_name = request.POST['last'], notes= request.POST['notes'])
    return redirect('/author')


#Default page for adding a book
def notes(request, id):
    context = {
        "author" : Author.objects.get(id=int(id)),
        "books": Book.objects.all()
    }
    return render(request, 'books_authors_app/notes.html', context)

def push_author (request, book_id):
    option = Author.objects.get(id = request.POST['push_author'])
    Book.objects.get(id = book_id).authors.add(option)
    return redirect(f"/description/{book_id}")

def push_book (request, author_id):
    option = Book.objects.get(id = request.POST['push_book'])
    Author.objects.get(id = author_id).books.add(option)
    return redirect(f"/notes/{author_id}")
    

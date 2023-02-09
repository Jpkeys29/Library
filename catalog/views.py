from django.shortcuts import render
#To return a simple "It's working" import HttpResponse
from django.http import HttpResponse
from .models import Book,Author,BookInstance,Genre,Language
from django.views.generic import CreateView, DetailView


# Create your views here.
def index(request):
    #Number of books
    num_books = Book.objects.all().count()
    #Number of actual copies
    num_instances = BookInstance.objects.all().count()
    #Number of copies available
    num_copies_available = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books':num_books,
        'num_instances': num_instances,
        'num_copies_available':num_copies_available
    }

    return render(request,'catalog/index.html',context=context)

#CRUD different from Class Book from models.py
class BookCreate(CreateView): #model_form.html
    model = Book #connects to the Book model
    fields = '__all__'

class BookDetail(DetailView):
    model = Book





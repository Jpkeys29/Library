from django.shortcuts import render
#To return a simple "It's working" import HttpResponse
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Book,Author,BookInstance,Genre,Language
from django.views.generic import CreateView, DetailView, ListView, DeleteView


# Create your views here.
def index(request):
    #Number of books(titles)
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
    #If you want to pass specific fields, create a list:
    #fields = ['first_name','last_name']

class BookDetail(DetailView):
    model = Book


#Read 
class BookList(ListView):
    model = Book
    field = '__all__'
    
#Delete
class BookDelete(DeleteView):
    #default template name: model_confirm-delete.html
    #It is a form that goes to confirm Delete Button
    model = Book
    #success_url is also an attribute and represents the URL you want to go to after the form has been submitted
    # success_url is NOT a template. It is the actual URL
    success_url = reverse_lazy('book_list')




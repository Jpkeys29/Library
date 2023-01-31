from django.db import models
from django.urls import reverse

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    #For Book and Author to be their own models, author is not only an attribute instead is going to be to an specific author(primary key):
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True) #on_delete, to delete author but not the book
    summary = models.TextField(max_length=600)
    #isbn(unique identifier for the book)
    isbn = models.CharField('ISBN', max_length=13,unique=True)
    #To connect a book to multiple genres(Genre class)Many-to_Many:
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.title

    #To access the record for an specific book. It returns an url:
    def get_absolute_url(self):
        return reverse('book_detail',kwargs={"pk":self.pk})


class Author(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    dob = models.DateField(null=True,blank=True)

    #To dictate order:
    class Meta:
        ordering= ['last_name','first_name']
    
    #To grab the url for the author:
    def get_absolute_url(self):
        return reverse('author_detail',kwargs={'pk:self.pk'})

    def __str__(self):
        return f"{self.last_name} , {self.first_name}"

#book instance model
#we need an unique identifier generator(uuid)It generates an unique id:
import uuid

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.RESTRICT,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateTimeField(null=True,blank=True)

    LOAN_STATUS = (
        ('m', 'Maintance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'




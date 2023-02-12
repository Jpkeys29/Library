#URLS Catalog views
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('create_book/',views.BookCreate.as_view(),name='create_book'),
    path('book/<int:pk>/',views.BookDetail.as_view(),name='book_detail'),
    path('book_list/', views.BookList.as_view(), name='book_list'),
    path('book_delete/<int:pk>',views.BookDelete.as_view(), name='book_delete'),
]
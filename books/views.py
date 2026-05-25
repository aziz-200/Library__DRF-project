from django.shortcuts import render
from .models import Book
from .Serializers import BookSerializer
from rest_framework import generics

# Create your views here.

class BookListApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    # serializer_class = BookSerializer
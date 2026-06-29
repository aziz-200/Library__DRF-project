from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .Serializers import BookSerializer
from rest_framework import generics, status


# Create your views here.

# class BookListApiView(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


#  APi manual case
class BookListApiView(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            'status': f'returned: {len(books)}',
            'books': serializer_data
        }
        return Response(data)


# get one item from all => retriveapi shu uchun ishlatiladi
# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data = {
            'status': "success",
            'book': serializer_data
        }
            return Response(data)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


#  Delete book => destroy api delete uchun ishlatiladi
# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            # book  = Book.objects.get_object_or_404(Book, pk=pk) => Bu usulda yozsa ham bo'ladi va TRY except kerak bo'lmaydi
            book = Book.objects.get(id=pk)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


#  Update book
# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id = pk)
        data = request.data
        serializer = BookSerializer(instance = book, data = data, partial = True)
        if serializer.is_valid(raise_exception=True):
            book_save = serializer.save()
        return Response(
            {
                'status': 'success',
                'book': book_save.id,

            }
        )


# Create book
class BookUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# CREATE BOOK
# class BookCreateApiView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApiView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = BookSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create book list
class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# FUNCTION based view in DRF
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)



       # for ModelVIEwsets  => url generate qilish uchun ishlatiladi
#  when should use -> CRUD , and manual works
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

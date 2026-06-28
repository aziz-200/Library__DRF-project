from rest_framework import serializers
from .models import Book

# serializer => formatni o'zgrtirib ma'lumotni formatlab beraid to json or other format
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book

        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn',  'price', )
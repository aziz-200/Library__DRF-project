from rest_framework import serializers
from .models import Book

# serializer => formatni o'zgrtirib ma'lumotni formatlab beraid to json or other format
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book

        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn',  'price', )


# Serializer orqali yozish, manual writting => and without meta class ,
# va modelga asoslanmagan holatlarda yozish tavsiya etiladi
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     subtitle = serializers.CharField(max_length=200)
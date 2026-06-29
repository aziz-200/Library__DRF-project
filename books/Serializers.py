from rest_framework import serializers
from .models import Book

# serializer => formatni o'zgrtirib ma'lumotni formatlab beraid to json or other format
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book

        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn',  'price', )

    # VALIDATION
    def validate(self, data):

        title = data.get('title', None)
        author = data.get('author', None)



        #  check title if  it contains only alphaber
        if not title.isalpha():
            raise serializers.ValidationError("Title must be alphanumeric")

        # check title, and author from DB
        if Book.objects.filter(title__iexact=title, author__iexact=author).exists():
            raise serializers.ValidationError("Title already exists")

        return data


# FIELD VALIDATION => faqat fieldni validate qiladi
    def validate_price(self, price):
        if price <= 0 or price > 1000:
            raise serializers.ValidationError("Price must be greater than 0")
        return price









# Serializer orqali yozish, manual writting => and without meta class ,
# va modelga asoslanmagan holatlarda yozish tavsiya etiladi
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     subtitle = serializers.CharField(max_length=200)
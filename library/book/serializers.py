from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'count', 'authors']
        extra_kwargs = {
            'authors': {'allow_empty': True, 'required': False}
        }

    def create(self, validated_data):
        authors = validated_data.pop('authors', [])
        book = Book.objects.create(**validated_data)
        book.authors.set(authors)
        return book

    def update(self, instance, validated_data):
        authors = validated_data.pop('authors', None)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.count = validated_data.get('count', instance.count)
        instance.save()
        if authors is not None:
            instance.authors.set(authors)
        return instance

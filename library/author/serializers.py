from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'patronymic']

    def create(self, validated_data):
        return Author.objects.create(**validated_data)
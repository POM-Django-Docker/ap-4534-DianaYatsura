from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
                    'id', 'email', 'first_name', 'middle_name', 'last_name',
                    'role', 'is_active', 'created_at', 'updated_at', 'password'
                ]
        extra_kwargs = {
                        'password': {'write_only': True},
                        }

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance


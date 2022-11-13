from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    @staticmethod
    def validate_username(username):
        if User.objects.filter(username=username):
            raise ValidationError('User with this username already exists')
        return username

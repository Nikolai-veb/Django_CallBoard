from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSer(serializers.ModelSerializer):
    """Для стериализацыи профиля"""
    class Meta:
        model = User
        fields = ("username", "email")





class ProfileSer(serializers.ModelSerializer):
    """Для вывода профиля"""

    user = UserSer
    class Meta:
        model = Profile
        fields = ("user", "avatar", "email_two", "phone", "first_name", "last_name")




class ProfileUpdateSer(serializers.ModelSerializer):
    """Для бновления профиля пользователя"""

    class Meta:
        model = Profile
        fields = ("avatar", "email_two", "phone", "first_name", "last_name")

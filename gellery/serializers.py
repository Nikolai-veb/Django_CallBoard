from rest_framework import serializers
from .models import *



class PhotoSer(serializers.ModelSerializer):
    """Модель для показа изоброженния"""
    class Meta:
        model = Photo
        fields = ("image", )




class GellerySer(serializers.ModelSerializer):
    """Для вывода галлереи """

    photos = PhotoSer(many=True, read_only=True)

    class Meta:
        model = Gellery
        fields = ("photos", )

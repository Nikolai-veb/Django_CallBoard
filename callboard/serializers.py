from rest_framework import serializers
from .models import *


class AdvertSer(serializers.ModelSerializers):
    """Модель для показа обьявлений"""
    class Meta:
        model = Advert
        fields = ("category", "filtres", "subject", "images", "price", "created")

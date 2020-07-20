from rest_framework import serializers
from .models import *
from gellery.serializers import GellerySer


class CategorySer(serializers.ModelSerializer):
    """Модель для показа категорий"""
    class Meta:
        model = Category
        fields = ("name",)



class FilterAdvertSer(serializers.ModelSerializer):
    """Модель для показа фильтров"""
    class Meta:
        model = FilterAdvert
        fields = ("name",)


class AdvertListSer(serializers.ModelSerializer):
    """Модель для показа обьявлений"""

    category = CategorySer()
    filtres = FilterAdvertSer()
    images = GellerySer()
    class Meta:
        model = Advert
        fields = ("id", "category", "filtres", "subject", "images", "price", "created", "slug")




class AdvertDetailSer(serializers.ModelSerializer):
    """Модель для показа обьявлений"""

    category = CategorySer()
    filtres = FilterAdvertSer()
    images = GellerySer()
    class Meta:
        model = Advert
        fields = (
            "category",
            "filtres",
            "subject",
            "description",
            "files",
            "images",
            "price",
            "created",
            "user",
        )





class AdvertCreateSer(serializers.ModelSerializer):
    """Для добавления обЪявления"""

    class Meta:
        model = Advert
        fields = (
            "category",
            "filtres",
            "subject",
            "description",
            "date",
            #"files",
            #"images",
            "price",
            #"created",
            #"user",
        )


        def create(self, request):
            request["user"] = self.context['request'].user
            advert = Advert.objects.create(**request)
            return advert


























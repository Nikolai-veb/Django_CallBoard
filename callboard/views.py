from django.shortcuts import render
<<<<<<< HEAD
from .models import Advert, Category
from django.views.generic import ListView, DetailView, View


class AdvertListView(ListView):
    """Обьявления"""
    model = Advert
    queryset = Advert.object.all()


class AdvertDetailView9(DetailView):
    """Подробно об обьявлениях"""
    model = Advert

=======
from .models import Advert, Category, AdvertFilter, 
>>>>>>> a3c357b237774505ea7552b6a06233b50aa02a01

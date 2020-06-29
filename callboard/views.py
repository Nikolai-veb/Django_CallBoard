from django.shortcuts import render
from .models import Advert, Category
from django.views.generic import ListView, DetailView, View


class AdvertListView(ListView):
    """Обьявления"""
    model = Advert
    queryset = Advert.object.all()


class AdvertDetailView9(DetailView):
    """Подробно об обьявлениях"""
    model = Advert


from django.shortcuts import render
from .models import Advert, Category
from django.views.generic import ListView, DetailView, View


class AdvertListView(ListView):
    """Обьявления"""
    model = Advert
    queryset = Advert.objects.all()


class AdvertDetailView(DetailView):
    """Подробно об обьявлениях"""
    model = Advert
    context_object_name = "advert"


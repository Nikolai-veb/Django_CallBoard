from .serializers import AdvertSer.
from .models import Advert, Category
from rest_framework import generics
from rest_framework import permissions

class AdvertListView(generics.ListAPIView):
    """Обьявления"""

    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()
    serializers_classes = AdvertSer

#class AdvertDetailView(DetailView):
  #  """Подробно об обьявлениях"""
   # model = Advert
    #context_object_name = "advert"


from .serializers import AdvertListSer, AdvertDetailSer, AdvertCreateSer
from .models import Advert, Category
from rest_framework import generics
from rest_framework import permissions

class AdvertListView(generics.ListAPIView):
    """Обьявления"""

    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()
    serializer_class = AdvertListSer

class AdvertDetailView(generics.RetrieveAPIView):
    """Подробно об обьявлениях"""

    permission_classes = [permissions.AllowAny]
    serializer_class = AdvertDetailSer
    queryset = Advert.objects.all()
    lookup_field = "slug"


class AdvertCreateView(generics.CreateAPIView):
    """Добавление обЪявления"""

    permission_classes = [permissions.IsAuthenticated]
    queryset = Advert.objects.all()
    serializer_class = AdvertCreateSer




from django.shortcuts import render

from .models import Profile
from rest_framework import generics, permissions
from .serializers import ProfileSer, ProfileUpdateSer

from callboard.models import Advert
from callboard.serializers import AdvertListSer, AdvertCreateSer


class ProfileDetail(generics.RetrieveAPIView):
    """Профиль пользователя"""

    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializers_class = ProfileSer




class ProfileUpdateView(generics.UpdateAPIView):
    """Для бновления профиля пользователя"""

    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializers_class = ProfileUpdateSer



class UserAdvertListView(generics.ListAPIView):
    """Все объявления пользователя"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertListSer

    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)


class UserAdvertUpdateView(generics.UpdateAPIView):
    """Для редактирования объявлений ользователя"""

    permission_classes = [permissions.IsAuthenticated]
    serializers_class = AdvertCreateSer

    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)




from django.shortcuts import render

from .models import Profile
from rest_framework import generics, permissions
from .serializers import ProfileSer, ProfileUpdateSer

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

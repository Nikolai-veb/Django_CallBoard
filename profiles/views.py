from django.shortcuts import render

from .models import Profile
from django.views.generic import ListView, DetailView


class ProfileDetail(DetailView):
    """Профиль пользователя"""
    model = Profile
    context_objeckt_name = 'profile'
    template_name = "profile/profile_detail.html"

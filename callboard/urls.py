from django.urls import path
from .views import *


urlpatterns = [
    path("", AdvertListView.as_view(), name="advert_list"),
    path("<slug:slug>/", AdvertDetailView.as_view(), name="advert_detail"),


]

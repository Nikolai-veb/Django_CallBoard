from django.urls import path

from .views import *

urlpatterns = [
    path("<slug:slug>/", ProfileDetail.as_view(), name="profile_detail")

]

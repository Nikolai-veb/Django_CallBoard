from django.urls import path

from .views import *

urlpatterns = [
    path("<slug:slug>/", ProfileDetail.as_view()),
    path("update/<slug:slug>/", ProfileUpdateView.as_view()),

]

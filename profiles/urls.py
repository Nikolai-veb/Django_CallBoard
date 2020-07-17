from django.urls import path

from .views import *

urlpatterns = [
    path("<int:pk>/", ProfileDetail.as_view()),
    path("update/<int:pk>/", ProfileUpdateView.as_view()),
    path("adverts/", UserAdvertListView.as_view()),
    path("update-adverts/<int:pk>/", UserAdvertUpdateView.as_view()),
]

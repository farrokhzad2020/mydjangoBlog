from django.urls import path
from . import views

urlpatterns = [
path('', views.films_list),
]

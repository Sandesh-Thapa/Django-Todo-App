from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('delete/<str:id>', views.delete_todo, name="delete"),
]
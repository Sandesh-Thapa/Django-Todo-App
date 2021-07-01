from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name="home"),
    path('delete/<str:id>', views.delete_todo, name="delete"),
    path('update/<str:id>', views.update_todo, name="update"),
]
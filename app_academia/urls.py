from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('treinos', views.treinos, name='treinos'),
]

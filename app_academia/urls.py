from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('treinos', views.treinos, name='treinos'),
    path('listar', views.listar, name='listar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('excluir/<int:id>', views.excluir, name='excluir'),
]

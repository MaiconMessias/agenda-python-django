from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('pesquisacliente/', views.pesquisacliente, name='pesquisacliente'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:cliente_id>/', views.editar, name='editar'),
    path('salvar/', views.salvar, name='salvar'),
    path('deletar/<int:cliente_id>/', views.deletar, name='deletar'),
    path('telalogin/', views.telalogin, name='telalogin'),
    path('logar/', views.logar, name='logar'),
    path('logout_view/', views.logout_view, name='logout_view'),
    #path('<int:cliente_id>/', views.adicionar, name='adicionar'),
    #path('<int:cliente_id>/results/', views.excluir, name='excluir'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:cliente_id>/', views.editar, name='editar'),
    path('salvar/', views.salvar, name='salvar'),
    path('deletar/<int:cliente_id>/', views.deletar, name='deletar'),
    
    #path('<int:cliente_id>/', views.adicionar, name='adicionar'),
    #path('<int:cliente_id>/results/', views.excluir, name='excluir'),
]
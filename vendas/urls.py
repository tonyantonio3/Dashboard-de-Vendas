from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),

    #PRODUTOS
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo/', views.criar_produto, name='criar_produto'),
    path('produtos/<int:id>/editar/', views.editar_produto, name='editar_produto'),
    path('produtos/<int:id>/excluir/', views.excluir_produto, name='excluir_produto'),

    #VENDAS
    path('vendas/', views.lista_vendas, name='lista_vendas'),
    path('vendas/nova/', views.criar_venda, name='criar_venda'),
    path('vendas/editar/<int:id>/', views.editar_venda, name='editar_venda'),
    path('vendas/excluir/<int:id>/', views.excluir_venda, name='excluir_venda'),
]
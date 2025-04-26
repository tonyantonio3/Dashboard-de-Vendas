from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/novo/', views.criar_produto, name='criar_produto'),
    path('produtos/<int:id>/editar/', views.editar_produto, name='editar_produto'),
    path('produtos/<int:id>/excluir/', views.excluir_produto, name='excluir_produto')
]
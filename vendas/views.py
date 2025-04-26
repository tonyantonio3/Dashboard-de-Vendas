from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm


def index(request):
    """Página inicial"""
    return render(request, 'index.html')

def lista_produtos(request):
    produtos = Produto.objects.all()
    context = {'produtos': produtos}
    return render(request, 'lista_produtos.html', context)

def criar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')

    else:
        form = ProdutoForm()

    return render(request, 'form_produto.html', {'form':form})

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')

    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'form_produto.html', {'form':form})

def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'confirmar_exclusao.html', {'produto':produto})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Venda, Cliente
from .forms import ProdutoForm, VendaForm
from django.contrib import messages


def index(request):
    """Página inicial"""
    return render(request, 'index.html')

# ================ CRUD Produto ================


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


# ================ CRUD Vendas ================

#Read
def lista_vendas (request):
    vendas = Venda.objects.all()
    context = {'vendas': vendas}
    return render (request, 'lista_vendas.html', context)

#Create
def criar_venda(request):
    if request.method == "POST":
        form = VendaForm(request.POST)
        if form.is_valid():
            venda = form.save(commit=False)
            venda.total = venda.total_venda()
            produto = venda.produto
            produto.estoque -= venda.quantidade
            produto.save()

            venda.save()
            messages.success(request, "Venda realizada com sucesso!")
            return redirect('lista_vendas')
    
    else:
        form = VendaForm()
    
    return render(request, 'form_venda.html', {'form': form})

#Update
def editar_venda(request, id):
    venda = get_object_or_404(Venda, id=id)
    if request.method == "POST":
         form = VendaForm(request.POST, instance=venda)
         if form.is_valid():
             venda = form.save(commit=False)
             venda.total = venda.total_venda()
             venda.save()
             return redirect('lista_vendas')
    
    else:
        form = VendaForm(instance=venda)

    return render(request, 'form_venda.html', {'form':form})

#Delete
def excluir_venda(request, id):
    venda = get_object_or_404(Venda, id=id)
    if request.method == "POST":
        venda.delete()
        return redirect('lista_vendas')
    
    return render(request, 'confirmar_exclusao_venda.html', {'venda':venda})

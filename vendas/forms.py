from django import forms
from .models import Produto, Venda

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'categoria']


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['produto', 'cliente', 'quantidade']

    def clean_quantidade(self):
        quantidade = self.cleaned_data.get('quantidade')
        produto = self.cleaned_data.get('produto')

        if produto.estoque < quantidade:
            raise forms.ValidationError(f'Não há estoque suficiente. Estoque disponível: {produto.estoque}.')
        return quantidade

    def save(self, commit=True):
        venda = super().save(commit=False)
        produto = venda.produto
        quantidade = venda.quantidade
        venda.total = produto.preco * quantidade

        if commit:
            venda.save()

            produto.estoque -= quantidade
            produto.save()

        return venda
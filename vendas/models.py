from django.db import models



class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    quantidade = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.produto.nome} - {self.cliente.nome}'

    def total_venda(self):
        if self.produto and self.quantidade:
            return float(self.quantidade) * float(self.produto.preco)
        return 0




from django.contrib import admin
from .models import Produto, Cliente, Venda

# Register your models here.

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Venda)




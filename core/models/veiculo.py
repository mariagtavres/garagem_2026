from django.db import models
from .modelo import Modelo
from .cor import Cor
from .acessorios import Acessorios


class Veiculo(models.Model):
    ano = models.IntegerField(default=0,  null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True, blank=True)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE, null=True, blank=True)
    acessorios = models.ManyToManyField(Acessorios, blank=True)

    def __str__(self):
        return f"{self.id} - {self.modelo} - {self.ano} - {self.cor}"
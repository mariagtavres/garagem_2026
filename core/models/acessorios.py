from django.db import models

class Acessorios (models.Model):
    descricao = models.CharField(max_length=100) 

    class Meta:
        verbose_name = 'Acessório'
        verbose_name_plural = 'Acessórios'

    def __str__(self):
        return f'({self.id}) {self.descricao}'
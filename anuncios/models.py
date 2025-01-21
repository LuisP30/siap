from django.db import models
from autenticacao.models import Anunciante

class Seguimento(models.Model):
    nome = models.CharField('Nome:', max_length=100)
    
    def __str__(self):
        return self.nome

class Anuncio(models.Model):
    titulo = models.CharField('Título:', max_length=100)
    descricao = models.CharField('Descrição:', max_length=200)
    preco_anterior = models.DecimalField('Preço Anterior:', max_digits=10, decimal_places=2)
    preco_atual = models.DecimalField('Preço Atual:', max_digits=10, decimal_places=2)
    validade = models.DateField('Duração da Promoção:')
    anunciante = models.ForeignKey(Anunciante, on_delete=models.DO_NOTHING)
    seguimento = models.ForeignKey(Seguimento, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.titulo




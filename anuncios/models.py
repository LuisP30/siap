from django.db import models


class Seguimento(models.Model):
    nome = models.CharField('Nome:', max_length=100)

class Anunciante(models.Model):
    empreendimento = models.CharField('Empreendimento:', max_length=150)
    cnpj = models.CharField('CNPJ:', max_length=14)
    endereco = models.CharField('Endereço:', max_length=200)
    telefone = models.CharField('Telefone:', max_length=11)
    email = models.CharField('Email:', max_length=50)
    whatsapp = models.URLField('Whatsapp:', max_length=200)
    instagram = models.URLField('Instagram:', max_length=200)

class Anuncio(models.Model):
    titulo = models.CharField('Título:', max_length=100)
    descricao = models.CharField('Descrição:', max_length=200)
    preco_anterior = models.DecimalField('Preço Anterior:', max_digits=10, decimal_places=2)
    preco_atual = models.DecimalField('Preço Atual:', max_digits=10, decimal_places=2)
    validade = models.DateField('Duração da Promoção:')
    anunciante = models.ForeignKey(Anunciante, on_delete=models.PROTECT)
    seguimento = models.ForeignKey(Seguimento, on_delete=models.PROTECT)

class Foto(models.Model):
    foto = models.ImageField(upload_to='media/')
    anuncio = models.ForeignKey(Anuncio, on_delete=models.PROTECT)



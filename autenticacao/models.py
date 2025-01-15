from django.db import models
from django.contrib.auth.models import AbstractUser

class Anunciante(AbstractUser):
    email = models.EmailField('E-mail', null=False, blank=False, unique=True)
    empreendimento = models.CharField('Empreendimento', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=14, null=True, blank=True, unique=True)
    endereco = models.CharField('Endereço', max_length=50, null=False)
    telefone = models.CharField('Telefone', max_length=11, null=False)
    whatsapp = models.CharField('WhatsApp', max_length=100, null=True, blank=True, unique=True)
    instagram = models.CharField('Instagram', max_length=100, null=True, blank=True, unique=True)
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'empreendimento', 'cnpj', 'endereco', 'telefone', 'whatsapp', 'instagram']
    
    def __str__(self):
        return self.empreendimento
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

class Anunciante(AbstractUser):
    username = models.CharField('Nome do empreendimento', max_length=45, null=False, unique=True, validators=[UnicodeUsernameValidator()])
    email = models.EmailField('E-mail', null=False, blank=False, unique=True)
    cnpj = models.CharField('CNPJ', max_length=14, null=True, blank=True, unique=True)
    endereco = models.CharField('Endereço', max_length=50, null=False)
    telefone = models.CharField('Telefone', max_length=11, null=False)
    whatsapp = models.CharField('WhatsApp', max_length=45, null=True)
    instagram = models.CharField('Instagram', max_length=45, null=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'endereco', 'telefone', 'whatsapp', 'instagram']
    
    def normaliza_instagram(self, username):
        username = username.strip()
        if "instagram.com/" in username:
            username = username.split("instagram.com/")[-1]
        if username.startswith("@"):
            username = username[1:]
        return username
    
    def save(self, *args, **kwargs):
        if self.instagram:
            self.instagram = self.normaliza_instagram(self.instagram)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username
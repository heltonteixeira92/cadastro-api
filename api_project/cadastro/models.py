from django.db import models


class CadastroCli(models.Model):
    NomeFantasia = models.CharField(max_length=250)
    RazaoSocial = models.CharField(max_length=250)
    CNPJ = models.CharField(max_length=20)
    Email = models.CharField(max_length=150)
    Telefone = models.CharField(max_length=30)
    DataCadastro = models.DateTimeField(auto_now_add=True)

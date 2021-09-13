from .models import CadastroCli
from rest_framework import serializers


class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroCli
        fields = ['id', 'NomeFantasia', 'RazaoSocial', 'CNPJ', 'Email', 'Telefone', 'DataCadastro']

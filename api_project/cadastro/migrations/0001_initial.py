# Generated by Django 3.2.7 on 2021-09-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroCli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomeFantasia', models.CharField(max_length=250)),
                ('RazaoSocial', models.CharField(max_length=250)),
                ('CNPJ', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=150)),
                ('Telefone', models.CharField(max_length=30)),
                ('DataCadastro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

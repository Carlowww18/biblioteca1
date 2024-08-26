# Generated by Django 5.0.7 on 2024-07-26 17:11

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
        ('usuarios', '0002_rename_usuario_usuarios_alter_usuarios_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='livros',
            options={'verbose_name': 'Livro'},
        ),
        migrations.RemoveField(
            model_name='livros',
            name='nome_emprestado',
        ),
        migrations.RemoveField(
            model_name='livros',
            name='tempo_duracao',
        ),
        migrations.AddField(
            model_name='livros',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuarios'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='livros',
            name='co_autor',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_cadastro',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livros',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuarios')),
            ],
        ),
        migrations.AddField(
            model_name='livros',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='livro.categoria'),
            preserve_default=False,
        ),
    ]

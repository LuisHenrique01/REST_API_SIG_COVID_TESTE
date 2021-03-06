# Generated by Django 3.0.7 on 2020-06-17 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_morbidades'),
    ]

    operations = [
        migrations.CreateModel(
            name='CasosPorDia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(unique=True, verbose_name='Dia')),
                ('confirmados', models.IntegerField(verbose_name='Confirmados')),
                ('obitos', models.IntegerField(verbose_name='Óbitos')),
                ('novosCasosPorDia', models.IntegerField(verbose_name='Novos Casos Por Dia')),
                ('novosObitosPorDia', models.IntegerField(verbose_name='Novos Óbitos Por Dia')),
            ],
        ),
    ]

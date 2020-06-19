# Generated by Django 3.0.7 on 2020-06-15 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='numCasosObitosCidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=50, verbose_name='Município')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('confirmados', models.IntegerField(verbose_name='Confirmados')),
                ('obitos', models.IntegerField(verbose_name='Óbitos')),
                ('incidencia', models.FloatField(verbose_name='Incidência')),
                ('populacao', models.IntegerField(null=True, verbose_name='População')),
            ],
        ),
    ]

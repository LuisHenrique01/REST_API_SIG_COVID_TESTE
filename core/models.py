from django.db import models
# Create your models here.

class numCasosObitosCidade(models.Model):
    municipio = models.CharField(max_length=50, verbose_name='Município')
    cep = models.CharField(max_length=9, verbose_name='CEP')
    confirmados = models.IntegerField(verbose_name='Confirmados')
    obitos = models.IntegerField(verbose_name='Óbitos')
    incidencia = models.FloatField(verbose_name='Incidência')
    populacao = models.IntegerField(verbose_name='População', null=True)
    data_coleta = models.DateField(verbose_name='Data de coleta')
    
    def __str__(self):
        return self.municipio
    
    
class TestesRapidos(models.Model):
    negativos = models.IntegerField(verbose_name='Teste Rápido Não Reagente')
    positivos = models.IntegerField(verbose_name='Teste Rápido Reagente')
    total = models.IntegerField(verbose_name='Total TR')
    data_coleta = models.DateField(verbose_name='Data de coleta')
    
    def __str__(self):
        return self.total
    
    
class ConfirmadosSexo(models.Model):
    masculino = models.IntegerField(verbose_name='Masculino')
    feminino = models.IntegerField(verbose_name='Feminino')
    data_coleta = models.DateField(verbose_name='Data de coleta')
    
    def __str__(self):
        return self.data_coleta.isoformat()
        
    
class ObitosSexo(models.Model):
    masculino = models.IntegerField(verbose_name='Masculino')
    feminino = models.IntegerField(verbose_name='Feminino')
    data_coleta = models.DateField(verbose_name='Data de coleta')
    
    def __str__(self):
        return self.data_coleta.isoformat()
    
    
class FaixaEtaria(models.Model):
    faixa = models.CharField(verbose_name="Faixa Etária", max_length=50)
    confirmados = models.IntegerField(verbose_name='Confirmados')
    obitos = models.IntegerField(verbose_name='Óbitos')
    percentual_conf = models.FloatField(verbose_name='Percentual Confirmados')
    percentual_obt = models.FloatField(verbose_name='Percentual Óbitos')
    data_coleta = models.DateField(verbose_name='Data de coleta')
    
    def __str__(self):
        return self.faixa
    
    
class Morbidades(models.Model):
    morbidade = models.CharField(verbose_name="Faixa Etária", max_length=50)
    quantidade = models.IntegerField(verbose_name='Quantidade')
    percentual = models.FloatField(verbose_name='Percentual')
    data_coleta = models.DateField(verbose_name='Data de coleta')
    
    def __str__(self):
        return self.morbidade
    
    
class CasosPorDia(models.Model):
    dia = models.DateField(verbose_name="Dia", unique=True)
    confirmados = models.IntegerField(verbose_name='Confirmados')
    obitos = models.IntegerField(verbose_name='Óbitos')
    novosCasosPorDia = models.IntegerField(verbose_name='Novos Casos Por Dia')
    novosObitosPorDia = models.IntegerField(verbose_name='Novos Óbitos Por Dia')
    
    def __str__(self):
        return self.dia.isoformat()
    
    
class CasosPorSemana(models.Model):
    semana = models.IntegerField(verbose_name="Semana", unique=True)
    confirmados = models.IntegerField(verbose_name='Confirmados')
    obitos = models.IntegerField(verbose_name='Óbitos')
    novos = models.IntegerField(verbose_name='Novos casos por semana')
    
    def __str__(self):
        return self.dia.isoformat()
    
    
class Leitos(models.Model):
    dia = models.DateField(verbose_name="Dia", unique=True)
    capacidade_leitos_clinicos = models.IntegerField(verbose_name='Capacidade leitos clinicos')
    internados_leitos_clinicos = models.IntegerField(verbose_name='Internados leitos clinicos')
    capacidade_UTI = models.IntegerField(verbose_name='Capacidade UTI')
    internados_UTI = models.IntegerField(verbose_name='Internados UTI')
    capacidade_leitos_estabilizacao = models.IntegerField(verbose_name='Capacidade leitos estabilização')
    internados_leitos_estabilizacao = models.IntegerField(verbose_name='Internados leitos estabilização')
    capacidade_leitos_respiradores = models.IntegerField(verbose_name='Capacidade leitos respiradores')
    internados_leitos_respiradores = models.IntegerField(verbose_name='Internados leitos respiradores')
    altas = models.IntegerField(verbose_name='Altas', null=True)
    
    def __str__(self):
        return self.dia.isoformat()

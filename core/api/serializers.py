from rest_framework.serializers import ModelSerializer
from core.models import CasosPorDia, CasosPorSemana, ConfirmadosSexo, FaixaEtaria, HistoricoCidade, Leitos, Morbidades, ObitosSexo, TestesRapidos, numCasosObitosCidade


class NumCasosObitosCidadeSerializer(ModelSerializer):
    class Meta:
        model = numCasosObitosCidade
        fields = ['municipio', 'cep', 'confirmados', 'obitos', 
                  'incidencia', 'populacao', 'data_coleta']


class TestesRapidosSerializer(ModelSerializer):
    class Meta:
        model = TestesRapidos
        fields = ['negativos', 'positivos', 'total', 'data_coleta']
        

class ConfirmadosSexoSerializer(ModelSerializer):
    class Meta:
        model = ConfirmadosSexo
        fields = ['masculino', 'feminino', 'data_coleta']
        
        
class ObitosSexoSerializer(ModelSerializer):
    class Meta:
        model = ObitosSexo
        fields = ['masculino', 'feminino', 'data_coleta']
        
        
class FaixaEtariaSerializer(ModelSerializer):
    class Meta:
        model = FaixaEtaria
        fields = ['faixa', 'confirmados', 'percentual_conf', 
                  'obitos', 'percentual_obt', 'data_coleta']
        
        
class MorbidadesSerializer(ModelSerializer):
    class Meta:
        model = Morbidades
        fields = ['morbidade', 'quantidade', 'percentual', 'data_coleta']
        

class CasosPorDiaSerializer(ModelSerializer):
    class Meta:
        model = CasosPorDia
        fields = ['dia', 'confirmados', 'obitos', 'novosCasosPorDia', 'novosObitosPorDia']
  
  
class CasosPorSemanaSerializer(ModelSerializer):
    class Meta:
        model = CasosPorSemana
        fields = ['semana', 'confirmados', 'obitos', 'novos']
  
  
class LeitosSerializer(ModelSerializer):
    class Meta:
        model = Leitos
        fields = ['dia', 'capacidade_leitos_clinicos', 'internados_leitos_clinicos', 
                  'capacidade_UTI', 'internados_UTI', 'capacidade_leitos_estabilizacao',
                  'internados_leitos_estabilizacao', 'capacidade_leitos_respiradores', 
                  'internados_leitos_respiradores', 'altas']
        
        
class HistoricoCidadeSerializer(ModelSerializer):
    class Meta:
        model = HistoricoCidade
        fields = ['data', 'municipio', 'confirmados', 'obitos', 'cep', 'ibge_id']
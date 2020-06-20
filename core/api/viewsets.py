from rest_framework.viewsets import ModelViewSet
from core.models import CasosPorDia, CasosPorSemana, ConfirmadosSexo, FaixaEtaria, HistoricoCidade, Leitos, Morbidades, ObitosSexo, TestesRapidos, numCasosObitosCidade
from core.api.serializers import NumCasosObitosCidadeSerializer, TestesRapidosSerializer, CasosPorSemanaSerializer
from core.api.serializers import CasosPorDiaSerializer, ConfirmadosSexoSerializer, FaixaEtariaSerializer, HistoricoCidadeSerializer, LeitosSerializer, MorbidadesSerializer, ObitosSexoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class NumCasosObitosCidadeViewSet(ModelViewSet):
    queryset = numCasosObitosCidade.objects.all()
    serializer_class = NumCasosObitosCidadeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['cep', 'confirmados', 'obitos', 'incidencia', 'populacao', 'data_coleta']
    search_fields = ['municipio']
    
    
class TestesRapidosViewSet(ModelViewSet):
    queryset = TestesRapidos.objects.all()
    serializer_class = TestesRapidosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data_coleta']
    
    
class ConfirmadosSexoViewSet(ModelViewSet):
    queryset = ConfirmadosSexo.objects.all()
    serializer_class = ConfirmadosSexoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data_coleta']
    
    
class ObitosSexoViewSet(ModelViewSet):
    queryset = ObitosSexo.objects.all()
    serializer_class = ObitosSexoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data_coleta']
    
    
class FaixaEtariaViewSet(ModelViewSet):
    queryset = FaixaEtaria.objects.all()
    serializer_class = FaixaEtariaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['data_coleta']
    search_fields = ['faixa']
    
    
class MorbidadesViewSet(ModelViewSet):
    queryset = Morbidades.objects.all()
    serializer_class = MorbidadesSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['data_coleta']
    search_fields = ['morbidade']
    
    
class CasosPorDiaViewSet(ModelViewSet):
    queryset = CasosPorDia.objects.all()
    serializer_class = CasosPorDiaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dia']
    
    
class CasosPorSemanaViewSet(ModelViewSet):
    queryset = CasosPorSemana.objects.all()
    serializer_class = CasosPorSemanaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['semana']    
    
    
class LeitosViewSet(ModelViewSet):
    queryset = Leitos.objects.all()
    serializer_class = LeitosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dia']     
    
    
class HistoricoCidadeViewSet(ModelViewSet):
    queryset = HistoricoCidade.objects.all()
    serializer_class = HistoricoCidadeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['data', 'cep', 'ibge_id']
    search_fields = ['municipio']     
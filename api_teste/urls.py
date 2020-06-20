"""api_teste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.api.viewsets import NumCasosObitosCidadeViewSet, TestesRapidosViewSet, MorbidadesViewSet
from core.api.viewsets import CasosPorDiaViewSet, CasosPorSemanaViewSet, ConfirmadosSexoViewSet, FaixaEtariaViewSet, HistoricoCidadeViewSet, LeitosViewSet, ObitosSexoViewSet

router = routers.DefaultRouter()
router.register(r'total-obitos-e-casos', NumCasosObitosCidadeViewSet)
router.register(r'total-testes-rapidos', TestesRapidosViewSet)
router.register(r'confirmados-sexo', ConfirmadosSexoViewSet)
router.register(r'obitos-sexo', ObitosSexoViewSet)
router.register(r'faixa-etaria', FaixaEtariaViewSet)
router.register(r'morbidades', MorbidadesViewSet)
router.register(r'casos-por-dia', CasosPorDiaViewSet)
router.register(r'casos-por-semanas', CasosPorSemanaViewSet)
router.register(r'leitos', LeitosViewSet)
router.register(r'historico-cidades', HistoricoCidadeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

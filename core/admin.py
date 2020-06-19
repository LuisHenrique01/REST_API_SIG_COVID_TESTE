from django.contrib import admin
from core.models import CasosPorDia, CasosPorSemana, ConfirmadosSexo, FaixaEtaria, Leitos, Morbidades, ObitosSexo, TestesRapidos, numCasosObitosCidade

# Register your models here.
admin.site.register(numCasosObitosCidade)
admin.site.register(TestesRapidos)
admin.site.register(ConfirmadosSexo)
admin.site.register(ObitosSexo)
admin.site.register(FaixaEtaria)
admin.site.register(Morbidades)
admin.site.register(CasosPorDia)
admin.site.register(CasosPorSemana)
admin.site.register(Leitos)
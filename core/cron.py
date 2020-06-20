from urllib import request
import csv
from core.models import CasosPorDia, CasosPorSemana, ConfirmadosSexo, FaixaEtaria, HistoricoCidade, Leitos, Morbidades, ObitosSexo, TestesRapidos, numCasosObitosCidade
from datetime import date
import re 
from unicodedata import normalize
import difflib
from core.cidades import cidades

'''
Faz o scrap dos dados da planilia
'''
def scrap_dados():
    data_atualizacao = get_data_atualizacao()
    atualiza_casos_obitos(data_atualizacao)
    atualiza_testes_rapidos(data_atualizacao)
    atualiza_confirmados_sexo(data_atualizacao)
    atualiza_obitos_sexo(data_atualizacao)
    atualiza_faixa_etaria(data_atualizacao)
    atualiza_morbidades(data_atualizacao)
    atualiza_casos_por_dia(data_atualizacao)
    atualiza_leitos(data_atualizacao)
    atualiza_historico(data_atualizacao)
    
    
def atualiza_casos_obitos(data_atualizacao):
    ultimo_registro = numCasosObitosCidade.objects.last()
    if ultimo_registro is None or ultimo_registro.data_coleta != data_atualizacao:
        nomeTabela, tabela = get_dict_dados(id_='532454257')
        bulk = []
        for municipio in tabela:
            #Os valores de incidencia, obitos, confirmados, populacao
            if municipio['Município'] == "PIAUÍ": 
                break
            bulk.append(numCasosObitosCidade(municipio=municipio['Município'], 
                                            confirmados=municipio['Confirmados'], 
                                            obitos=municipio['Óbitos'],
                                            incidencia=municipio['Incidência'].replace(',', '.'),
                                            populacao=municipio['População'],
                                            cep=municipio['CEP'],
                                            data_coleta=data_atualizacao))
        numCasosObitosCidade.objects.bulk_create(bulk)
                    
                    
def atualiza_testes_rapidos(data_atualizacao):
    ultimo_registro = TestesRapidos.objects.last()
    if  ultimo_registro is None or ultimo_registro.data_coleta != data_atualizacao:
        nomeTabela, tabela = get_dict_dados(id_='1934173117')
        bulk = []
        for linha in tabela:
            bulk.append(TestesRapidos(negativos=linha['Teste Rápido Não Reagente'], 
                                     positivos=linha['Teste Rápido Reagente'], 
                                     total=linha['Total TR'],
                                     data_coleta=data_atualizacao))
        TestesRapidos.objects.bulk_create(bulk)
                    
                    
def atualiza_confirmados_sexo(data_atualizacao):
    ultimo_registro = ConfirmadosSexo.objects.last()
    if  ultimo_registro is None or ultimo_registro.data_coleta != data_atualizacao:
        nomeTabela, tabela = get_dict_dados(id_='0')
        tabela = list(tabela)
        conf_sexo = ConfirmadosSexo(masculino=tabela[0]['Quantidade'], 
                                    feminino=tabela[1]['Quantidade'], 
                                    data_coleta=data_atualizacao)
        conf_sexo.save()                    
        
                    
def atualiza_obitos_sexo(data_atualizacao):
    ultimo_registro = ObitosSexo.objects.last()
    if  ultimo_registro is None or ultimo_registro.data_coleta != data_atualizacao:
        nomeTabela, tabela = get_dict_dados(id_='953543508')
        tabela = list(tabela)
        obt_sexo = ObitosSexo(masculino=tabela[0]['Quantidade'], 
                             feminino=tabela[1]['Quantidade'], 
                             data_coleta=data_atualizacao)
        obt_sexo.save()
                    
              
def atualiza_faixa_etaria(data_atualizacao):
    ultimo_registro = FaixaEtaria.objects.last()
    if  ultimo_registro is None or ultimo_registro.data_coleta != data_atualizacao:
        nomeTabela, tabela = get_dict_dados(id_='1402178422')
        bulk = []
        for linha in tabela:
            if linha['Faixa Etária'] == "TOTAL": 
                break
            bulk.append(FaixaEtaria(faixa=linha['Faixa Etária'], 
                                    confirmados=linha['Confirmados'], 
                                    obitos=linha['Óbitos'],
                                    percentual_conf=linha['Percentual C.'].replace(',', '.'),
                                    percentual_obt=linha['Percentual O.'].replace(',', '.'),
                                    data_coleta=data_atualizacao))
        FaixaEtaria.objects.bulk_create(bulk)
                    

def atualiza_morbidades(data_atualizacao):
    ultimo_registro = Morbidades.objects.last()
    if  ultimo_registro is None or ultimo_registro.data_coleta != data_atualizacao:
        nomeTabela, tabela = get_dict_dados(id_='687147050')
        bulk = []
        for linha in tabela:
            bulk.append(Morbidades(morbidade=linha['Morbidades'], 
                                    quantidade=linha['Qtde'],
                                    percentual=linha['Percentual'].replace(',', '.'),
                                    data_coleta=data_atualizacao))
        Morbidades.objects.bulk_create(bulk)

                                
def atualiza_casos_por_dia(data_atualizacao):
    ultimo_registro_dia = CasosPorDia.objects.last()
    ultimo_registro_semana = CasosPorSemana.objects.last()
    nomeTabela, tabela = get_dict_dados(id_='181109212')
    bulk_dia = []
    bulk_semana = []
    for linha in tabela:
        dia, mes = tuple(map(int, linha['Dias'].split('/')))
        ano = date.today().year
        data = date(ano, mes, dia)
        if  ultimo_registro_dia is None or ultimo_registro_dia.dia < data:
            obitos = linha['Óbitos'] if linha['Óbitos'] != '' else 0
            novosObitos = linha['Óbitos por dia'] if linha['Óbitos por dia'] != '' else 0
            bulk_dia.append(CasosPorDia(dia=data, 
                                    confirmados=linha['Confirmados'],
                                    obitos=obitos,
                                    novosCasosPorDia=linha['Novos por Dia'],
                                    novosObitosPorDia=novosObitos))
        semana = linha['Semana']
        if (semana != '') and (ultimo_registro_semana is None or ultimo_registro_semana.semana < int(semana)):
            bulk_semana.append(CasosPorSemana(semana=semana, 
                                                confirmados=linha['Conf/Semana'],
                                                obitos=linha['Obt/Semana'],
                                                novos=linha['Novos/Semana']))
    CasosPorDia.objects.bulk_create(bulk_dia)
    CasosPorSemana.objects.bulk_create(bulk_semana)


def atualiza_leitos(data_atualizacao):
    ultimo_registro_dia = Leitos.objects.last()
    nomeTabela, tabela = get_dict_dados(id_='1465700325')
    bulk = []
    for linha in (tabela):
        dia, mes, ano = tuple(map(int, linha['Dias'].split('/')))
        data = date(ano, mes, dia)
        if  ultimo_registro_dia is None or ultimo_registro_dia.dia < data:
            if linha['Altas'] != '':
                bulk.append(Leitos(dia=data, 
                                   capacidade_leitos_clinicos=linha['Capacidade Leitos Clínicos'],
                                   internados_leitos_clinicos=linha['Internados Leitos Clínicos'],
                                   capacidade_UTI=linha['Capacidade UTI'],
                                   internados_UTI=linha['Internados UTI'],
                                   capacidade_leitos_estabilizacao=linha['Capacidade LE'],
                                   internados_leitos_estabilizacao=linha['Internados Estabilização'],
                                   capacidade_leitos_respiradores=linha['Capacidade Leitos Respiradores'],
                                   internados_leitos_respiradores=linha['Internados Leitos Respiradores'],
                                   altas=linha['Altas']))
            else:
                bulk.append(Leitos(dia=data, 
                                   capacidade_leitos_clinicos=linha['Capacidade Leitos Clínicos'],
                                   internados_leitos_clinicos=linha['Internados Leitos Clínicos'],
                                   capacidade_UTI=linha['Capacidade UTI'],
                                   internados_UTI=linha['Internados UTI'],
                                   capacidade_leitos_estabilizacao=linha['Capacidade LE'],
                                   internados_leitos_estabilizacao=linha['Internados Estabilização'],
                                   capacidade_leitos_respiradores=linha['Capacidade Leitos Respiradores'],
                                   internados_leitos_respiradores=linha['Internados Leitos Respiradores']))
    Leitos.objects.bulk_create(bulk)
    
    
def atualiza_historico(data_atualizacao):
    ultimo_registro_dia = HistoricoCidade.objects.last()
    nomeTabela, tabela = get_dict_dados(id_='1655251943')
    bulk = []
    for linha in (tabela):
        dia, mes, ano = tuple(map(int, linha['DATA (Balanço do dia)'].split('/')))
        data = date(ano, mes, dia)
        if  ultimo_registro_dia is None or ultimo_registro_dia.dia < data:
            for nome, cidade in zip(cidades.keys(), cidades.values()):
                        if compara_cidades(nome, linha['MUNICÍPIO']):
                            obitos = linha['TOTAL DE ÓBITOS'] if linha['TOTAL DE ÓBITOS'] != '' else 0
                            bulk.append(HistoricoCidade(municipio=linha['MUNICÍPIO'],
                                                        data=data,
                                                        confirmados=linha['CASOS CONFIRMADOS'],
                                                        obitos=obitos,
                                                        ibge_id=cidade['codigo_ibge'],
                                                        cep=cidade['cep']))
    HistoricoCidade.objects.bulk_create(bulk)


def get_dict_dados(id_, url='https://docs.google.com/spreadsheets/d/1b-GkDhhxJIwWcA6tk3z4eX58f-f1w2TA2f2XrI4XB1w/export?format=csv&gid='):
    # URL do Google Spreadsheet do Painel Epidemiológico da Covid-19 - SESAPI
    dadosDaPagina = request.urlopen(url+id_) # 532454257 é o ID da base de dados 

    # Os dados obtidos através do urllib vêm no formato bytes.
    # Portanto, precisamos transformá-los em caracteres utf-8
    dadosDecodificados = []
    for row in dadosDaPagina:
        dadosDecodificados.append(row.decode('utf-8'))

    dic_Dados = csv.DictReader(dadosDecodificados)
    cabecalhoDaTabela = dic_Dados.fieldnames
    return cabecalhoDaTabela, dic_Dados


def get_data_atualizacao():
    cabecalhoAtualizacao, dic_atualizacao = get_dict_dados(id_='1514947706')
    atualizacao = list(dic_atualizacao)[0]['Data']
    p = re.compile(r'\d+')
    datas = p.findall(atualizacao)
    isoFormattedDate = datas[2] + '-' + datas[1] + '-' + datas[0]

    data_atualizacao = date.fromisoformat(isoFormattedDate)
    return data_atualizacao


def padronizar_cidade(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII').lower()


def compara_cidades(*args):
    cidade1, cidade2 = map(padronizar_cidade, args)

    min_percent_equal = 95
    diff = difflib.SequenceMatcher(None, cidade1, cidade2)
    percent_equal = round(diff.ratio(), 5) * 100

    return percent_equal >= min_percent_equal
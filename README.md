# REST_API_SIG_COVID_TESTE
Testes realizados para a REST API do SIG COVID

# 1 - Instalação:

* Baixando a API

```bash
git clone https://github.com/LuisHenrique01/REST_API_SIG_COVID_TESTE.git
```
* Criando o ambiente virtual    
   * Observação: Python >= 3.7

```bash
python -m venv venv
```

```bash
 source venv/bin/activate 
```

# 2 - Configurando
* Instalando dependências
```bash
 pip install -r requirements.txt
```

* Configurando o banco de dados (SQLite, para ultilizar o Postgres faça as devidas conecções e execute os comandos abaixo)

```bash
 python manage.py makemigrations
```
```bash
 python manage.py migrate
```
# 3 - Buscando dados na SESAPI

* Entrando no shell do Django 

```bash
 python manage.py shell
```
* Estraindo os dados e salvando no banco
```python
from core.cron import scrap_dados
scrap_dados()
exit()
```

# 4 - Iniciando

```bash
 python manage.py runserver
```

# 5 - Modo de usar

* Entrar no link [API TESTE](http://127.0.0.1:8000/).

* Lá está listados links para endpoints da API (links para informções a serem solicitada).
   * "Total de casos e obitos": "http://127.0.0.1:8000/total-obitos-e-casos/",
   * "Total de testes rapidos": "http://127.0.0.1:8000/total-testes-rapidos/",
   * "Confirmados por sexo": "http://127.0.0.1:8000/confirmados-sexo/",
   * "Óbitos por sexo": "http://127.0.0.1:8000/obitos-sexo/",
   * "Faixa etária": "http://127.0.0.1:8000/faixa-etaria/",
   * "Morbidades": "http://127.0.0.1:8000/morbidades/",
   * "Casos por dia(Somatorio do estado)": "http://127.0.0.1:8000/casos-por-dia/",
   * "Casos por semanas(Somatorio do estado)": "http://127.0.0.1:8000/casos-por-semanas/",
   * "Numero de leitos": "http://127.0.0.1:8000/leitos/",
   * "Historico por cidades": "http://127.0.0.1:8000/historico-cidades/"

* Para obter os dados é só entrar no link pelo navegador ou fazer um GET diretamente da sua aplicação em qualquer linguagem. 

* Para ultilizar os filtros é so acrescentar um "?" após a URL.
   * Exemplos: 
      * Simples: http://127.0.0.1:8000/total-obitos-e-casos/?cep=64748000
      * Mais de um campo: http://127.0.0.1:8000/total-obitos-e-casos/?cep=64748000&data_coleta=2020-06-15
      * Para nomes de cidades: http://127.0.0.1:8000/total-obitos-e-casos/?search=Arraial

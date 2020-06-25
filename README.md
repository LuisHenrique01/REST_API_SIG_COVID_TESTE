# REST_API_SIG_COVID_TESTE
Testes realizados para a REST API do SIG COVID

# 1 - Instalação: 
* git clone https://github.com/LuisHenrique01/REST_API_SIG_COVID_TESTE.git

* python -m venv venv (Python >= 3.7)

* source venv/bin/activate 

* pip install -r requirements.txt

# 2 - Configurando

* python manage.py makemigrations

* python manage.py migrate

* python manage.py shell

* Estraindo os dados e salvando em banco
  * from core.cron import scrap_dados
  * scrap_dados()
  * exit()

# 3 - Iniciando

* python manage.py runserver

# 4 - Modo de usar

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
   * Exemplo: http://127.0.0.1:8000/total-obitos-e-casos/?cep=64748000
   * Mais de um campo: http://127.0.0.1:8000/total-obitos-e-casos/?cep=64748000&data_coleta=2020-06-15
   * Para nomes de cidades: http://127.0.0.1:8000/total-obitos-e-casos/?search=Arraial

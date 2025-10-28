from bs4 import BeautifulSoup

class ReclameAquiScraper:
    def __init__(self):
        pass

    def parse_pagina_principal(self, pagina_html):

        #Analisa o html da pagina com BeatifulSoup
        #Extrai os urls das melhores e piores empresas

        soup = BeautifulSoup(pagina_html, 'html.parser')

        tag_titulo = 'data-testeid'
        texto_titulo_melhores = 'ranking'
        texto_titulo_piores = 'ranking'

        urls_melhores_empresas = []
        urls_piores_empresas = []

        print("Scraper: Analisando página principal...")

        return urls_melhores_empresas, urls_piores_empresas
    
    def parse_pagina_empresa(self, pagina_html):

        #Analisa o html da pagina de uma empresa
        #Extrai as informacoes relevantes da empresa

        soup = BeautifulSoup(pagina_html, 'html.parser')

        dados_empresa = {} #dicionario para armazenar os dados da empresa
        
        #todo: logica para extrair os dados da empresa

        print("Scraper: Analisando página da empresa...")

        return dados_empresa
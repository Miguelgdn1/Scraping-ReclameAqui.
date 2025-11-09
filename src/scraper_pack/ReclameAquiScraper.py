from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import time

class ReclameAquiScraper:
    def __init__(self):
        self.driver = uc.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.URL_BASE = "https://www.reclameaqui.com.br"
        self.RANKINGS = ("Melhores", "Piores")

    def carregar_pagina(self):
        self.driver.get(self.URL_BASE)
        time.sleep(2)

    def esperar_por_elemento(self, by, value,):
        try:
            elemento = self.wait.until(
                EC.presence_of_element_located((by, value))
            )
            return elemento
        except TimeoutException:
            print(f"Elemento {value} não encontrado.")
            return None
        
    def scrape_hrefs(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        links = soup.select('a[data-testid="listing-ranking"]')
        hrefs = [link.get("href") for link in links if link.get("href")]
        # print(hrefs)
        return hrefs

        
    def selecionar_categoria(self, nome_categoria):
        input_categoria = self.esperar_por_elemento(By.XPATH, "//input[@placeholder='Selecione ou busque uma categoria']")
        self.driver.execute_script("arguments[0].click();", input_categoria)
        time.sleep(1)
        
        opcao_categoria = self.esperar_por_elemento(By.XPATH, f"//button[@title='{nome_categoria}']")
        self.driver.execute_script("arguments[0].click();", opcao_categoria)
        time.sleep(1)

    def is_valido(self, ele):
        if ele == "--":
            return False
        return True

    def extrair_percentuais(self, texto):
        percentual = None
        for ele in texto.split():
            if ele[-1] == '%':
                elemento = ele[:-1]
                if self.is_valido(elemento):
                    return float(elemento)
                else:
                    return 0
        return percentual
    
    def extrair_nota(self, texto):
        ultimo_elemento = texto.split()[-1]
        ultimo_elemento = ultimo_elemento[:-1]
        if self.is_valido(ultimo_elemento):
            return float(ultimo_elemento)
        else:
            return 0
    
    def get_dados_empresa(self, href):
        #print(self.URL_BASE + href)
        self.driver.get(self.URL_BASE + href)
        time.sleep(2)

        self.esperar_por_elemento(By.ID, "newPerformanceCard")
        
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')

        spans = soup.find_all('span', class_='go2549335548')

        nota_texto = spans[3].text.strip()
        reclamacoes_respondidas_texto = spans[1].text.strip()
        voltariam_a_fazer_negocio_texto = spans[4].text.strip()
        reclamacoes_resolvidas_texto = spans[5].text.strip()
    
        nota_valor = self.extrair_nota(nota_texto)
        reclamacoes_respondidas_valor = self.extrair_percentuais(reclamacoes_respondidas_texto)
        voltariam_a_fazer_negocio_valor = self.extrair_percentuais(voltariam_a_fazer_negocio_texto)
        reclamacoes_resolvidas_valor = self.extrair_percentuais(reclamacoes_resolvidas_texto)

        dados_empresa = {
                        "nota": nota_valor,
                        "reclamacoes_respondidas_percentual": reclamacoes_respondidas_valor,
                        "voltariam_a_fazer_negocio_percentual": voltariam_a_fazer_negocio_valor,
                        "reclamacoes_resolvidas_percentual": reclamacoes_resolvidas_valor
                        }
        
        return dados_empresa

    def fechar(self):
        self.driver.quit()

    def selecionar_ranking(self, ranking):
        data_test_id = None

        if ranking == self.RANKINGS[0]:
            data_test_id = "tab-best"
        elif ranking == self.RANKINGS[1]:
            data_test_id = "tab-worst"

        ranking_input = self.esperar_por_elemento(By.XPATH, f"//li[@data-testid='{data_test_id}']")
        self.driver.execute_script("arguments[0].click();", ranking_input)
        time.sleep(2)

    def get_nome_empresa(self, href):
        return href.split('/')[-1]

    def scrape(self, categoria):
        try:
            dados_completos = {}
            for ranking in self.RANKINGS:
                self.carregar_pagina()
                self.esperar_por_elemento(By.CLASS_NAME, "ranking-segment")
                self.selecionar_categoria(categoria)
                self.selecionar_ranking(ranking)
                hrefs = self.scrape_hrefs()
                for href in hrefs:
                    nome_empresa = self.get_nome_empresa(href)
                    dados_completos[nome_empresa] = self.get_dados_empresa(href)
            return dados_completos

        except Exception as e:
            print(f"Error scrapping {self.URL_BASE}: {e}")
            return None
        finally:
            self.fechar()
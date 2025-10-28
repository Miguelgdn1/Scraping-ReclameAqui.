from selenium import webdriver
from selenium.webdriver.chrome.service import Service 

class BrowserManager:

    url = "https://www.reclameaqui.com.br"

    def __init__(self):
        self.driver = webdriver.Chrome()

    def abrir_site(self, url):
        self.driver.get(url)

    def conteudo_pagina(self):
        return self.driver.page_source

    def fechar_browser(self):
        self.driver.quit()
        
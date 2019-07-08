from os import system

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re

class Crawler:

    def __init__(self, cli=False):
        self.cli = cli
        self.driver = self._get_driver()

    def _get_driver(self):
        print('Iniciando Navegador')
        if self.cli:
            options = Options()
            options.headless = True
            return webdriver.Firefox(options=options, executable_path=r'C:\geckodriver.exe')
        return webdriver.Firefox()

    def acessar(self, url):
        print("Acessando: "+url)
        self.driver.get(url)
        return self

    def encontrar_link_texto(self,texto):
        print('procurando: '+texto)
        return self.driver.find_element_by_partial_link_text(texto)

    def encontrar_filho(self, pai, filho):
        print('procurando: '+filho)

        elemento_pai = self.driver.find_element_by_class_name(pai)
        return elemento_pai.find_element_by_class_name(filho)

    def encerrar(self):
        self.driver.quit()

crawler = Crawler()
crawler.acessar('https://horriblesubs.info/shows/')\
       .encontrar_link_texto('Enen no Shouboutai')\
       .click()
elemento = crawler.encontrar_filho('hs-shows', 'rls-info-container')
elemento.click()
elemento = elemento.find_element_by_class_name('link-1080p')
magnet = re.search('href="(magnet:.+?)&amp.+?">', elemento.get_attribute('innerHTML')).group(1)
system('deluge-console add '+magnet)
crawler.encerrar()